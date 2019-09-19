import random

import parameters
from agents import Agent


class RandomAgent(Agent):
    @staticmethod
    def next_choice():
        return random.randint(1, parameters.N_BOOKS)

    def choose_book(self):
        # Don't reread books (random.randint can be used if this rereading is desired) This is too slow!
        # options = [n for n in range(1, parameters.N_BOOKS + 1) if n not in self.read_books]
        # self.choice = random.choice(options)

        # TODO: This can cause problems if the search takes a long time (causing to chance of collision to increase)
        # Keeping track of a set of available options might be faster
        self.choice = self.next_choice()
        while self.choice in self.read_books:
            self.choice = self.next_choice()
