"""This is the `__main__` module."""
import random
from game import print_board, input_position, check_win

if __name__ == "__main__":
    CURRENT_PLAYER = random.choice(['o', 'x'])
    while True:
        print_board()
        check_win()
        input_position(CURRENT_PLAYER)
        if CURRENT_PLAYER == 'x':
            CURRENT_PLAYER = 'o'
        else:
            CURRENT_PLAYER = 'x'
