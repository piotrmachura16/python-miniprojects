from deck import Card, Deck


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
        pass
