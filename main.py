from simulation import Simulation
import statistics
from parameters_config import parameters

sim = Simulation(parameters)
energies = sim.run()
print("Energy used", str(statistics.mean(energies)))
