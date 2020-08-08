from tictactoe import print_board, input_position, check_win
import random

if __name__ == "__main__":
    current_player = random.choice(['o', 'x'])
    while True:
        print_board()
        check_win()
        input_position(current_player)
        if current_player == 'x':
            current_player = 'o'
        else:
            current_player = 'x'
