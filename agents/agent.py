import parameters


class Agent(object):
    def __init__(self, name, book_reads):
        self.gossip_protocol = None
        self.name = name
        self.energy = parameters.STARTING_ENERGY
        self.choice = 0
        self.read_books = set()
        self.book_reads = book_reads
        self.exhausted = False

    def choose_book(self):
        pass

    def use_energy(self, cost):
        self.energy -= cost
        if self.energy <= 0:
            self.exhausted = True

    def read(self):
        if self.exhausted:
            return False

        self.use_energy(parameters.READ_COST)
        self.book_reads[self.choice] += 1
        self.read_books.add(self.choice)

        return True

    def gossip(self, other: 'Agent'):
        if self.exhausted:
            return False

        self.use_energy(parameters.GOSSIP_COST)
        # get the union of the read lists
        self.read_books = self.read_books | other.read_books
        other.read_books = self.read_books

        return True
