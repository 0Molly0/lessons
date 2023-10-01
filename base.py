import random


class Library:
    def __init__(self, address: str, helmet: str) -> None:
        self.address: str = address.strip()
        self.director: str = 'Mr. ' + helmet.title().strip()
        self.books: list = []

    def __str__(self) -> str:
        return f'Library at {self.address}'

    def get_random_book(self) -> str:
        return random.choice(self.books)

    def __del__(self):
        print('Help me')
