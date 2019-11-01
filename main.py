from simulation import Simulation
import statistics
from parameters_config import parameters
import argparse
import graph_exporter

parser = argparse.ArgumentParser(description="Simulate gossip task division")

parser.add_argument('--iterations',
                    dest='iterations',
                    type=int,
                    action='store',
                    default=100,
                    help='How many iterations should the simulation run? (default is 100)')
parser.add_argument('--repeats',
                    dest='repeats',
                    type=int,
                    action='store',
                    default=20,
                    help='How many times should each iterations repeat? (default: 20)')
parser.add_argument('--readcosts',
                    dest='read_costs',
                    type=int,
                    action='store',
                    default=[1, 5, 10],
                    nargs='+',
                    help='What read costs should be used? Each value will be simulated separately. (default: 1 5 10)')
args = parser.parse_args()

if __name__ == '__main__':
    graph_exporter.test_all(args.iterations, args.repeats, args.read_costs)

# sim = Simulation(parameters, True)
# energies = sim.run()
