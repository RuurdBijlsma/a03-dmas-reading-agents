import random

from agents import Agent


class RandomAgent(Agent):
    def choose_book(self):
        upper_limit = self.parameters.n_books - len(self.read_books)
        random_unread_book = random.randint(1, 1 if upper_limit == 0 else upper_limit)

        for book in self.read_books:
            if book <= random_unread_book:
                random_unread_book += 1
            else:
                break

        self.choice = random_unread_book
