import csv
import os
from structures.parameters_structure import Parameters
from structures.simulation_result import SimulationResult
import gossip
import statistics
from multiprocessing import Pool
import multiprocessing as mp
from simulation import Simulation

data_directory = 'data'


def test_all(iterations=20, repeats=15, read_costs=None):
    if read_costs is None:
        read_costs = [1, 5, 10]
    print("Now running all tests\n")

    protocols = [gossip.LearnNewSecretsGossipProtocol(), gossip.TokenGossipProtocol(),
                 gossip.CallMeOnceGossipProtocol(), gossip.SpiderGossipProtocol()]

    i = 0
    for read_cost in read_costs:
        for protocol in protocols:
            i += 1
            to_print = "NOW TESTING '{}', READ COST: {}, ITERATIONS: {}, REPEATS PER ITERATION: {}, TEST {}/{}".format(
                str(protocol),
                read_cost,
                iterations,
                repeats, i,
                len(protocols) * len(read_costs))
            print('=' * len(to_print))
            print(to_print)
            print('=' * len(to_print))

            test(protocol, read_cost, iterations, repeats)

    print("\nAll tests complete")


def test(protocol, read_cost=5, iterations=20, repeats=15):
    p_from = Parameters(
        gossip_cost=1,
        read_cost=read_cost,
        n_agents=int(1),
        n_books=int(1000),
        gossip_protocol=protocol
    )
    p_to = Parameters(
        gossip_cost=1,
        read_cost=read_cost,
        n_agents=int(200),
        n_books=int(1000),
        gossip_protocol=protocol
    )

    results = run_multiple_simulations(p_from, p_to, iterations, repeats)

    get_lowest_energy(results)
    get_lowest_total_energy(results)

    export_results_to_csv("{}_{}_{}_{}".format(str(protocol), read_cost, iterations, repeats), results, p_from)


def get_lowest_energy(results):
    assert len(results) > 0

    lowest_energy = results[0].energy_per_agent
    lowest_result = results[0]

    for result in results:
        if result.energy_per_agent < lowest_energy:
            lowest_energy = result.energy_per_agent
            lowest_result = result

    print("Lowest energy per agent found was {}, optimal n_agents {}".format(lowest_energy,
                                                                             lowest_result.parameters.n_agents))
    return lowest_result


def get_lowest_total_energy(results):
    assert len(results) > 0

    lowest_energy = results[0].total_energy
    lowest_result = results[0]

    for result in results:
        if result.total_energy < lowest_energy:
            lowest_energy = result.total_energy
            lowest_result = result

    print("Lowest total energy found was {}, optimal n_agents {}".format(lowest_energy,
                                                                         lowest_result.parameters.n_agents))
    return lowest_result


def export_results_to_csv(experiment_name, results, parameters_from):
    from_dict = parameters_from.__dict__

    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    export_path = os.path.join(data_directory, experiment_name + '.csv')
    with open(export_path, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_keys = list(from_dict.keys())
        csv_keys.append('energy (mean)')
        csv_keys.insert(0, 'iteration')

        filewriter.writerow(results[0].to_csv_names())
        for result in results:
            filewriter.writerow(result.to_csv_row())

        print("Exported data to csv file: {}".format(export_path))


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

    pool = Pool(processes=mp.cpu_count())
    starmap_arguments = map(lambda ps: (
        ps,
        param_steps.index(ps) + 1,
        repeats_per_data_point), param_steps)
    return pool.starmap(simulate_parameters, starmap_arguments)


def simulate_parameters(parameters, iteration, repeats):
    energies_per_agent = []
    total_energies = []

    for i in range(repeats):
        energies = Simulation(parameters).run()

        energies_per_agent.append(statistics.mean(energies))
        total_energies.append(sum(energies))

    print("Iteration {} complete".format(iteration))

    return SimulationResult(parameters, statistics.mean(energies_per_agent), statistics.mean(total_energies), repeats)
