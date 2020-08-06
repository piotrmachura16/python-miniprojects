from random import sample


class Game:

    # CARDS - constant dictionary with card-value pairs
    CARDS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
             '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 10]}

    def __init__(self, balance):
        self.balance = balance
        self.hand = []

    def bet(self, amount):
        if balance - amount < 0:
            print(
                f"Not enough money to bet ${amount}. Current balance: ${self.balance}")
        else:
            balance -= amount
            print(f"Bet of ${amount} placed. Current balance: ${self.balance}")

    def stand(self):
        pass

    def hit(self, board=None):
        if board == None:
            board = []
        self.hand.append(sample(Game.CARDS.keys(), 1)[0])
        points = self.points(board)
        print(
            f'Hand:{self.hand} | Board: {board} current points: {points}')
        if type(points) == tuple:
            if points[0] > 21 and points[1] > 21:
                print('You busted!')
                raise Exception
        elif points > 21:
            print('You busted!')
            raise Exception

    def points(self, board):
        points1 = 0
        points10 = 0
        for card in self.hand + board:
            if card == 'Ace':
                points10 += Game.CARDS[card][0]
                points1 += Game.CARDS[card][1]
            else:
                points1 += Game.CARDS[card]
                points10 += Game.CARDS[card]
        if points1 != points10:
            return points1, points10
        else:
            return points1


p1 = Game(1000)

p1.hit()
p1.hit()
p1.hit()
