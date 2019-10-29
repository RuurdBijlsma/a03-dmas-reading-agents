from simulation import Simulation
import statistics
from parameters_config import parameters
import graph_exporter

if __name__ == '__main__':
    graph_exporter.test_all(50, 20)


# sim = Simulation(parameters, True)
# energies = sim.run()
