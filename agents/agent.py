import parameters


class Agent(object):
    def __init__(self, name):
        self.gossip_protocol = None
        self.name = name
        self.energy = 0
        self.choice = 0
        self.read_books = []

    def choose_book(self):
        pass

    def read(self):
        self.energy += parameters.READ_COST
        self.read_books.append(self.choice)

    def gossip(self, other: 'Agent'):
        self.energy += parameters.GOSSIP_COST
        # get the union of the read lists
        self.read_books = list(set(self.read_books) | set(other.read_books))
        other.read_books = self.read_books
