import random

import parameters
from agents import Agent


class TickingAgent(Agent):
    def __init__(self, name, book_reads, all_agents):
        super().__init__(name, book_reads)
        self.all_agents = all_agents

    def tick(self, time, secret):
        # Read a book every time step
        self.choose_book()
        self.read()
        if secret == self.choice:
            print("Book found!")
            return True

        for agent in self.all_agents:
            if agent == self:
                continue

            if self.gossip_protocol.can_gossip(agent):
                self.gossip(agent)

        # When iteration is done:
        self.gossip_protocol.next_iteration()

        return False

    def choose_book(self):
        random_unread_book = random.randint(1, parameters.N_BOOKS - len(self.read_books))

        for book in self.read_books:
            if book <= random_unread_book:
                random_unread_book += 1
            else:
                break

        self.choice = random_unread_book
