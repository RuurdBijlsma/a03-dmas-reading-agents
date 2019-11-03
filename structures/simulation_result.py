import statistics
from structures.parameters_structure import Parameters


# Structure to hold result of simulation result
class SimulationResult(object):
    def __init__(self, parameters=Parameters(), energy_per_agent=0, total_energy=0, repeats=0):
        self.parameters = parameters
        self.energy_per_agent = energy_per_agent
        self.total_energy = total_energy
        self.repeats = repeats

    # returns the column names of this class for csv
    @staticmethod
    def to_csv_names():
        return Parameters.to_csv_names() + ['energy_per_agent', 'total_energy']

    # Return column values of this object for csv
    def to_csv_row(self):
        return self.parameters.to_csv_row() + [self.energy_per_agent, self.total_energy]
