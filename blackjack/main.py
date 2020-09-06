"""This is the `__main__` module."""
import os
import sys
from deck import Deck
from player import Dealer, Human
from exception import BustedException, WinException
from exception import ExitException, FoldException


def print_header():
    """Prints the persistant header message from global `PLAYER` and `DEALER`
    variables.
    """
    global PLAYER
    global DEALER
    os.system('cls' if os.name == 'nt' else 'clear')
    print('--------------- BLACKJACK ---------------', end='\n\n')
    print(DEALER, end='\n\n')
    print(PLAYER, end='\n\n')
    print('-----------------------------------------')


def bet_or_exit():
    """Asks the user whether they want to `bet` or exit."""
    choice = input('Input your bet (0 to fold, q to exit): ')
    if choice == '0':
        raise FoldException()
    elif choice == 'q':
        raise ExitException()
    else:
        PLAYER.bet(int(choice))


def hit_or_stand():
    """Asks the user whether they want to `hit` or `stand`."""
    print('Choose your action:')
    print('[1] Hit [2] Stand [q] Quit ')
    while True:
        try:
            choice = int(input('Choose an option: '))
            break
        except ValueError:
            pass
    if choice == 0:
        print('Exiting...')
        sys.exit()
    elif choice == 1:
        PLAYER.hit(DECK, 1)


if __name__ == '__main__':
    DECK = Deck()
    DEALER = Dealer(DECK)
    PLAYER = Human(DECK, 1000)

    while True:
        print_header()
        try:
            bet_or_exit()
        except FoldException as ex:
            print(ex.messsage)
            continue
        except ValueError:
            continue
        while True:
            print_header()
            try:
                hit_or_stand()
            except BustedException as ex:
                print('Busted!')
                break
