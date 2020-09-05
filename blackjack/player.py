"""This module contains the `Player` class and the derivatives:
`Dealer` and `Human`.
"""
from deck import Card, Deck


class Player:
    """The parent `Player` class. Contains an extensive `__repr__` method and a
    `hit` method.
    """

    def __init__(self):
        self.hand = []
        self.balance = None
        self.name = ''

    def __repr__(self) -> str:
        str_repr = f'-- {self.name} --\n'
        str_repr += 'Hand: '
        for symbol in Card.TYPES.keys():
            counter = self.hand.count(Card(symbol))
            if counter != 0:
                str_repr += f'[{symbol}]: {counter} '
        str_repr += '\n'

        points, points_alt = self.calculate_points()
        if points == points_alt:
            str_repr += f'Points: {points} '
        else:
            str_repr += f'Points (Ace=1): {points}, '
            str_repr += f'Points (Ace=11): {points_alt} '

        if self.balance is not None:
            str_repr += '\n'
            str_repr += f'Balance: {self.balance}'

        return str_repr

    def __str__(self) -> str:
        return self.__repr__()

    def calculate_points(self) -> int:
        """Return current amount of points from cards in `self.hand`"""
        points = 0
        points_alt = 0
        for card in self.hand:
            points += card.value[0]
            points_alt += card.value[1]
        return points, points_alt

    def hit(self, deck: Deck, hwo_many: int):
        """Pop `n` cards from `deck` and add them to `self.cards`"""
        try:
            self.hand += [deck.pop() for _ in range(hwo_many)]
        except ValueError:
            # TODO: Handle error when the deck is empty
            pass


class Dealer(Player):
    """The Dealer class. Hits 1 card when created."""

    def __init__(self, deck: Deck):
        super().__init__()
        self.name = 'DEALER'
        self.hit(deck, 1)

    def hit_continuosly(self, deck: Deck, oponent: Player):
        """Hit until you have more points than `oponent` or until you exceed 21
        """
        while self.calculate_points() < 21:
            self.hit(deck, 1)
            points = self.calculate_points()
            oponent_points = oponent.calculate_points()
            if oponent_points < points <= 21:
                print(f'The {self.name} wins!')
                break
        else:
            print(f'The {oponent.name} wins!')


class Human(Player):
    """The Human class. Hits 2 cards when created. Extends `Player` with `bet`
    and `stand` methods
    """

    def __init__(self, deck: Deck, balance: int):
        super().__init__()
        self.name = 'HUMAN'
        self.balance = balance
        self.hit(deck, 2)

    def bet(self, amount: int) -> int:
        """Bet `amount` on winning the current hand."""
        if self.balance - amount < 0:
            print(f"Not enough money to bet ${amount}.")
        else:
            self.balance -= amount
            print(f"Bet of ${amount} placed.")
        print(f"Current balance: ${self.balance}")

    def stand(self):
        """Do nothing."""
