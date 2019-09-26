import random

import parameters
from agents import Agent


class RandomAgent(Agent):
    @staticmethod
    def next_choice():
        return random.randint(1, parameters.N_BOOKS)

    def choose_book(self):
        random_unread_book = random.randint(1, parameters.N_BOOKS - len(self.read_books))

        for book in self.read_books:
            if book <= random_unread_book:
                random_unread_book += 1
            else:
                break

        self.choice = random_unread_book
