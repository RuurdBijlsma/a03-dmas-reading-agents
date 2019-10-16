import csv
import os
from structures.parameters_structure import Parameters
from structures.simulation_result import SimulationResult
import gossip
import statistics
import threading
from multiprocessing import Pool
import multiprocessing as mp
from simulation import Simulation

data_directory = 'data'


def test():
    p_from = Parameters(
        gossip_cost=1,
        read_cost=5,
        n_agents=int(1),
        n_books=int(1000),
        gossip_protocol=gossip.LearnNewSecretsGossipProtocol
    )
    p_to = Parameters(
        gossip_cost=1,
        read_cost=5,
        n_agents=int(100),
        n_books=int(1000),
        gossip_protocol=gossip.CallMeOnceGossipProtocol
    )

    results = run_multiple_simulations(p_from, p_to, 20, 15)

    get_lowest_energy(results)
    export_results_to_csv('test_123', results, p_from)


def get_lowest_energy(results):
    assert len(results) > 0

    lowest_energy = results[0].energy
    lowest_result = Parameters()

    for result in results:
        if result.energy < lowest_energy:
            lowest_energy = result.energy
            lowest_result = result

    print("Lowest energy found was {}, optimal n_agents {}".format(lowest_energy, lowest_result.parameters.n_agents))
    return lowest_result


def export_results_to_csv(experiment_name, results, parameters_from):
    from_dict = parameters_from.__dict__

    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    with open(os.path.join(data_directory, experiment_name + '.csv'), 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_keys = list(from_dict.keys())
        csv_keys.append('energy (mean)')
        csv_keys.insert(0, 'iteration')

        filewriter.writerow(results[0].to_csv_names())
        for result in results:
            filewriter.writerow(result.to_csv_row())

        print("Exported data to csv file")


def run_multiple_simulations(parameters_from: Parameters, parameters_to: Parameters, n_data_points=50,
                             repeats_per_data_point=10):
    from_dict = parameters_from.__dict__
    to_dict = parameters_to.__dict__

    param_steps = []
    for i in range(n_data_points):
        param_step = Parameters()
        for key in from_dict:
            from_value = from_dict[key]
            to_value = to_dict[key]
            if isinstance(from_value, int):
                difference = to_value - from_value
                param_step.__setattr__(key, int(from_value + difference / (n_data_points - 1) * i))
            elif isinstance(from_value, (float, complex)):
                difference = to_value - from_value
                param_step.__setattr__(key, from_value + difference / (n_data_points - 1) * i)
            else:
                param_step.__setattr__(key, from_value)
        param_steps.append(param_step)

    print(
        "Started simulation for csv data, {} iterations, ".format(n_data_points) +
        "each iteration runs {} simulation(s)".format(repeats_per_data_point))

    pool = Pool(processes=mp.cpu_count())
    starmap_arguments = map(lambda ps: (
        ps,
        param_steps.index(ps) + 1,
        repeats_per_data_point), param_steps)
    return pool.starmap(simulate_parameters, starmap_arguments)


def simulate_parameters(parameters, iteration, repeats):
    energies = []
    for i in range(repeats):
        energies.append(statistics.mean(Simulation(parameters).run()))
    #     also add the total energy consumption

    print("Simulation step {} complete".format(iteration))

    return SimulationResult(parameters, energies)
