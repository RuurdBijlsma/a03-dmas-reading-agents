import random

from agents import RandomAgent
from gossip import SpiderGossipProtocol, TokenGossipProtocol, LearnNewSecretsGossipProtocol


class Simulation(object):
    def __init__(self, parameters, log=False):
        assert parameters.n_agents is not 0
        self.parameters = parameters
        self.log = log
        self.secret = random.randint(1, self.parameters.n_books)
        self.agents = []
        self.book_reads = {}
        # Create agents that pick randomly and communicate using a Call Me Once protocol
        self.reset()

    def reset(self):
        self.agents = []
        self.book_reads = {}
        for i in range(1, self.parameters.n_books + 1):
            self.book_reads[i] = 0

        for i in range(0, self.parameters.n_agents):
            agent = RandomAgent(i, self.book_reads, self.parameters)
            # agent.gossip_protocol = self.parameters.gossip_protocol(agent)
            self.agents.append(agent)

    def run(self):
        self.print("Agents will now start searching books for the secret")
        self.print(
            "Protocol: {}, book count: {}, agent count: {}".format(self.parameters.gossip_protocol.__class__.__name__,
                                                                   self.parameters.n_books,
                                                                   self.parameters.n_agents))
        self.print(
            "\nStarting simulation, each iteration every agent will read a random" +
            " book which hasn't already been read in the previous iterations" +
            "\nAt the end of each iteration the agents share which books have been read via gossip")
        iteration = 1

        secret_found = False
        while True:
            self.print("Iteration {}".format(iteration))

            for agent in self.agents:
                agent.choose_book()
                agent.read()

            # run gossip protocol
            self.gossip_all(self.parameters.gossip_protocol)

            # provided the gossiping works, each agent has the same list of read books, unless some agents are exhausted
            # assert (len(set(map(lambda a: len(a.read_books), self.agents))) == 1)

            agents_knowing_secret = 0

            for agent in self.agents:
                if self.secret in agent.read_books:
                    agents_knowing_secret += 1

            if agents_knowing_secret > 0:
                if self.parameters.all_agents_must_know:
                    if isinstance(self.parameters.gossip_protocol, (SpiderGossipProtocol, TokenGossipProtocol)):
                        self.gossip_all(LearnNewSecretsGossipProtocol)

                self.print("secret found: {}".format(self.secret))
                self.print("The number of agents knowing the secrets is {}".format(agents_knowing_secret))
                break

            for agent in self.agents:
                self.parameters.gossip_protocol.next_iteration(agent)

            iteration += 1

        duplicate_reads = 0
        duplicate_book_reads = 0
        books_read = 0

        for key in self.book_reads:
            if self.book_reads[key] > 0:
                books_read += 1
            if self.book_reads[key] > 1:
                duplicate_reads += self.book_reads[key] - 1
                duplicate_book_reads += 1

        self.print("\nRead books (synchronized between all agents via gossip): {}".format(self.agents[0].read_books))
        self.print("Read {} out of {} books".format(books_read, self.parameters.n_books))
        self.print("{} books were read more than once".format(duplicate_book_reads))
        self.print("{} redundant reads were performed (book was already read when reading)".format(duplicate_reads))

        return list(map(lambda a: a.energy, self.agents))

    def gossip_all(self, protocol):
        for agent in self.agents:
            for other in self.agents:
                if agent == other:
                    continue

                if protocol.can_gossip(agent, other):
                    agent.gossip(other)

    # In the case of many simulations being run, we don't want to spam the program output with simulation messages
    def print(self, message):
        if self.log:
            print(message)
