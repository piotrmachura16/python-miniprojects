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
        try:
            return self.symbol == o.symbol
        except Exception:
            return False

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
        self.cards = 4*[Card(symbol) for symbol in Card.TYPES.keys()]

    def __len__(self) -> int:
        return len(self.cards)

    def __repr__(self) -> str:
        str_repr = 'Deck:\n'
        for symbol in Card.TYPES.keys():
            counter = self.cards.count(Card(symbol))
            if counter != 0:
                str_repr += f'[{symbol}]: {counter} '
        return str_repr

    def __str__(self) -> str:
        return self.__repr__()

    def pop(self) -> Card:
        """Return a random card from `self.cards`, removing it from the deck."""
        return self.cards.pop(randrange(len(self)))


class Player:
    def __init__(self):
        self.hand = []
        self.balance = None
        self.name = ''

    def __repr__(self) -> str:
        str_repr = self.name + '\n'
        str_repr += 'Hand: '
        for symbol in Card.TYPES.keys():
            counter = self.hand.count(Card(symbol))
            if counter != 0:
                str_repr += f'[{symbol}]: {counter} '
        str_repr += '\n'

        points = 0
        points_alt = 0
        for card in self.hand:
            points += card.value[0]
            points_alt += card.value[1]
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

    def hit(self, deck: Deck, n: int):
        """Pop `n` cards from `deck` and add them to `self.cards`"""
        try:
            self.hand += [deck.pop() for _ in range(n)]
        except ValueError:
            # TODO: Handle error when the deck is empty
            pass


class Dealer(Player):
    """The Dealer class. Hits 1 card when created."""

    def __init__(self, deck: Deck):
        super().__init__()
        self.name = '-- DEALER --'
        self.hit(deck, 1)


class Human(Player):
    """The Human class. Hits 2 cards when created. Extends `Player` with `bet`
    and `stand` methods
    """

    def __init__(self, deck: Deck, balance: int):
        super().__init__()
        self.name = '-- HUMAN --'
        self.balance = balance
        self.hit(deck, 2)

    def bet(self, amount: int):
        """Bet `amount` on winning the current hand."""
        if self.balance - amount < 0:
            print(f"Not enough money to bet ${amount}.")
            print(f"Current balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Bet of ${amount} placed.")
            print(f"Current balance: ${self.balance}")

    def stand(self):
        """Do nothing."""
        pass


deck = Deck()
dealer = Dealer(deck)
player = Human(deck, 2000)
print(deck)
print(dealer)
print(player)
