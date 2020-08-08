import os

# Global variable board is a 0-9 list, which eventually get replaced with x/o
board = list(range(9))


def print_board():
    """Clear the terminal screen and print the board."""

    global board
    # Clear the screen with cls (Windows) or clear (other systems)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print the board
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('----------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('----------')
    print(f'{board[6]} | {board[7]} | {board[8]}', end='\n\n')


def input_position(player):
    """Ask the `player` for position. Exit if `input==q`."""

    while True:
        try:
            pos_string = input(f'{player}: ')
            if pos_string == 'q':
                exit()
            position = int(pos_string)
            if position in board:
                board[position] = player
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid position, try again or "q" to quit.')


def check_win():
    """Check if there is a winner (or draw) and end the game if there is."""

    global board
    h_index = 0
    v_index = 0
    # Check horizontal lines with h_index and vertical lines with v_index
    for _ in range(0, 3):
        if board[h_index] == board[h_index + 1] == board[h_index + 2]:
            print(f'{board[h_index]} won!')
            exit()
        if board[v_index] == board[v_index + 3] == board[v_index + 6]:
            print(f'{board[v_index]} won!')
            exit()
        h_index += 3
        v_index += 1

    # Check diagonals
    if board[0] == board[4] == board[8]:
        print(f'{board[0]} won!')
        exit()
    if board[2] == board[4] == board[6]:
        print(f'{board[2]} won!')
        exit()
    # Check if the board is NOT full
    for cell in board:
        if str(cell) in '012345678':
            break
    # If full draw the game
    else:
        print('Draw!')
        exit()
