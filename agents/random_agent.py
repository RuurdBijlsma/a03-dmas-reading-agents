import random

import parameters
from agents import Agent


class RandomAgent(Agent):
    def choose_book(self):
        # Don't reread books (random.randint can be used if this rereading is desired)
        options = [n for n in range(1, parameters.N_BOOKS + 1) if n not in self.read_books]
        self.choice = random.choice(options)
