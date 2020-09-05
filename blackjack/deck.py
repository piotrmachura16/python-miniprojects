"""This module contains the `Card` as well as `Deck` classes.
"""
from random import randrange


class Card:
    """The Card class. Contains fields `symbol` (string) and a `value` (tuple).
    The static `TYPES` dictonary contains pairs of all of the valid symbols and
    values.
    """

    def __init__(self, symbol: str):
        self.symbol = symbol
        self.value = self.TYPES[self.symbol]

    def __repr__(self) -> str:
        return self.symbol

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Card) and self.symbol == o.symbol

    TYPES = {'2': (2, 2),
             '3': (3, 3),
             '4': (4, 4),
             '5': (5, 5),
             '6': (6, 6),
             '7': (7, 7),
             '8': (8, 8),
             '9': (9, 9),
             '10': (10, 10),
             'Jack': (10, 10),
             'Queen': (10, 10),
             'King': (10, 10),
             'Ace': (1, 11)
             }


class Deck:
    """The Deck class. Contains field `cards` (list of 52 `Card`) and a method
    `pop`.
    """

    def __init__(self):
        self.cards = 4*[Card(symbol) for symbol in Card.TYPES]

    def __len__(self) -> int:
        return len(self.cards)

    def __repr__(self) -> str:
        str_repr = 'Deck:\n'
        for symbol in Card.TYPES:
            counter = self.cards.count(Card(symbol))
            if counter != 0:
                str_repr += f'[{symbol}]: {counter} '
        return str_repr

    def __str__(self) -> str:
        return self.__repr__()

    def pop(self) -> Card:
        """Return a random card from `self.cards`, removing it from the deck."""
        return self.cards.pop(randrange(len(self)))
