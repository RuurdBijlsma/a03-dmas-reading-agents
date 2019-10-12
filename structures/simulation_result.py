import statistics
from structures.parameters_structure import Parameters


class SimulationResult(object):
    def __init__(self, parameters, energies):
        self.parameters = parameters
        self.energies = energies
        self.energy = statistics.mean(energies)
        self.repeats = len(energies)

    @staticmethod
    def to_csv_names():
        return Parameters.to_csv_names() + ['energy']

    def to_csv_row(self):
        return self.parameters.to_csv_row() + [self.energy]
