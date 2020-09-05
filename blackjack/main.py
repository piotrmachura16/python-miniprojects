"""This is the `__main__` module."""
import os
import sys
from deck import Deck
from player import Dealer, Human

if __name__ == '__main__':
    deck = Deck()
    dealer = Dealer(deck)
    player = Human(deck, 1000)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('------------------------ BLACKJACK ------------------------', end='\n\n')
        print(dealer, end='\n\n')
        print(player, end='\n\n')
        print('------------')
        if player.calculate_points()[0] > 21:
            print('Busted!')
            sys.exit()
        print('[1] Hit [2] Stand [0] Quit ')
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
            player.hit(deck, 1)
