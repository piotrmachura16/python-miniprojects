"""This module contains the game rules."""
import os
import sys

# Global variable board is a 0-9 list, which eventually get replaced with x/o
BOARD = list(range(9))


def print_board():
    """Clear the terminal screen and print the board."""

    global BOARD
    # Clear the screen with cls (Windows) or clear (other systems)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print the board
    print(f'{BOARD[0]} | {BOARD[1]} | {BOARD[2]}')
    print('----------')
    print(f'{BOARD[3]} | {BOARD[4]} | {BOARD[5]}')
    print('----------')
    print(f'{BOARD[6]} | {BOARD[7]} | {BOARD[8]}', end='\n\n')


def input_position(player):
    """Ask the `player` for position. Exit if `input==q`."""

    while True:
        try:
            pos_string = input(f'{player}: ')
            if pos_string == 'q':
                sys.exit()
            position = int(pos_string)
            if position in BOARD:
                BOARD[position] = player
                break
            raise ValueError
        except ValueError:
            print('Invalid position, try again or "q" to quit.')


def check_win():
    """Check if there is a winner (or draw) and end the game if there is."""

    global BOARD
    h_index = 0
    v_index = 0
    # Check horizontal lines with h_index and vertical lines with v_index
    for _ in range(0, 3):
        if BOARD[h_index] == BOARD[h_index + 1] == BOARD[h_index + 2]:
            print(f'{BOARD[h_index]} won!')
            sys.exit()
        if BOARD[v_index] == BOARD[v_index + 3] == BOARD[v_index + 6]:
            print(f'{BOARD[v_index]} won!')
            sys.exit()
        h_index += 3
        v_index += 1

    # Check diagonals
    if BOARD[0] == BOARD[4] == BOARD[8]:
        print(f'{BOARD[0]} won!')
        sys.exit()
    if BOARD[2] == BOARD[4] == BOARD[6]:
        print(f'{BOARD[2]} won!')
        sys.exit()
    # Check if the board is NOT full
    for cell in BOARD:
        if str(cell) in '012345678':
            break
    # If full draw the game
    else:
        print('Draw!')
        sys.exit()
