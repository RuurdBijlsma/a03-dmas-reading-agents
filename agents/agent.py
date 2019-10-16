class Agent(object):
    def __init__(self, name, book_reads, parameters):
        self.gossip_protocol = None
        self.parameters = parameters
        self.name = name
        self.energy = 0
        # self.token = True
        self.choice = 0
        self.read_books = set()
        self.book_reads = book_reads

    def choose_book(self):
        pass

    def use_energy(self, cost):
        self.energy += cost

    def read(self):
        self.use_energy(self.parameters.read_cost)
        self.book_reads[self.choice] += 1
        self.read_books.add(self.choice)

        return True

    def gossip(self, other: 'Agent'):
        self.use_energy(self.parameters.gossip_cost)
        # get the union of the read lists
        self.read_books = self.read_books | other.read_books
        other.read_books = self.read_books

        return True
