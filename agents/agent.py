class Agent(object):
    def __init__(self, name, book_reads, parameters):
        self.parameters = parameters
        self.name = name
        # Every agent has energy, goes up as they do things like reading and gossiping
        self.energy = 0

        # Protocol related properties
        self.token = True
        self.called = []

        # Book that the agent will read, is set by choose_book
        self.choice = 0
        # Books that have been read by this agent
        self.read_books = set()
        # Reference to book reads dictionary, which stores which books have multiple reads etc.
        self.book_reads = book_reads

    def choose_book(self):
        pass

    def use_energy(self, cost):
        self.energy += cost

    def read(self):
        # Read book function, use read_cost energy
        self.use_energy(self.parameters.read_cost)
        # Set book read in the dictionary
        self.book_reads[self.choice] += 1
        self.read_books.add(self.choice)

        return True

    def gossip(self, other: 'Agent'):
        self.use_energy(self.parameters.gossip_cost)
        # Set the read books of this agent and the gossiping agent to the union of both read_books set
        self.read_books = self.read_books | other.read_books
        other.read_books = self.read_books

        return True
