import random

from agents import Agent


class RandomAgent(Agent):
    def choose_book(self):
        unread_books_count = self.parameters.n_books - len(self.read_books)

        # If there are no unread books, choose a random book
        # Else pick an unread book
        if unread_books_count == 0:
            self.choice = random.randint(1, self.parameters.n_books)
            return

        random_unread_book = random.randint(1, unread_books_count)

        for book in self.read_books:
            if book <= random_unread_book:
                random_unread_book += 1
            else:
                break

        self.choice = random_unread_book
