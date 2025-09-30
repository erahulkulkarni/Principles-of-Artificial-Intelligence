"""
Solve the Tic-Tac-Toe problem
"""
"""
    noughts and crosses
    
    Game Structure, Components
        Board, 3 x 3 grid to represent the game state
        Players, two players, represented by 'X' and 'O'
        Input, get player input and validate move
        Win(Draw) Check, determine if a player has won the game
"""

"""
    Careful, there is a whitespace between single quotes ' '
    
    It is 'whitespace'          ' '
    and not a empty string      ''
"""
board = [' ' for _ in range(9)]     # Initialize the board with empty spaces

"""
    -------------
    |   |   |   |
    -------------
    |   |   |   |
    -------------
    |   |   |   |
    -------------

Python uses zero-based indexing
    Players asked to enter move(location) values inbetween 1 to 9
    To use this input in program, input value is subtracted by 1

board, as seen by
             Players    and by    Program
         -------------         -------------
         | 1 | 2 | 3 |         | 0 | 1 | 2 |
         -------------         -------------
         | 4 | 5 | 6 |         | 3 | 4 | 5 |
         -------------         -------------
         | 7 | 8 | 9 |         | 6 | 7 | 8 |
         -------------         -------------
"""

line = "-------------"
def print_board():    # Print the current state of the Tic Tac Toe board
    print("\n", line)
    for i, j, k in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
        print(f" | {board[i]} | {board[j]} | {board[k]} |\n", line)


"""
Winning combinations (for 'X', and the same is true with respect to 'O'):

    Horizontal -------------    or   -------------    or   -------------
               | X | X | X |         |   |   |   |         |   |   |   |
               -------------         -------------         -------------
               |   |   |   |         | X | X | X |         |   |   |   |
               -------------         -------------         -------------
               |   |   |   |         |   |   |   |         | X | X | X |
               -------------         -------------         -------------

    Vertical   -------------    or   -------------    or   -------------
               | X |   |   |         |   | X |   |         |   |   | X |
               -------------         -------------         -------------
               | X |   |   |         |   | X |   |         |   |   | X |
               -------------         -------------         -------------
               | X |   |   |         |   | X |   |         |   |   | X |
               -------------         -------------         -------------         

    Diagonal   -------------    or   -------------
               | X |   |   |         |   |   | X |
               -------------         -------------
               |   | X |   |         |   | X |   |
               -------------         -------------
               |   |   | X |         | X |   |   |
               -------------         -------------
"""
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                        (0, 4, 8), (2, 4, 6)]             # Diagonal

def check_win(player):          # Check if the given player has won the game
    for combo in winning_combinations:             # 8 combinations to check
        if all(board[i] == player for i in combo):   # Is all of, Horizontal
            return True         # or Vertical, or Diagonal same player value
    return False


def check_draw():                              # Check if the game is a draw
    return ' ' not in board                 # No empty spaces exist in board


def play_game():                            # main game loop for Tic Tac Toe
    current_player = 'X'  # 'X' will be swapped with 'O' (and vice versa) later
    game_over = False

    while not game_over:
        print_board()
        
        move = int(input(f"Player {current_player}, enter your move (1-9): "))
        
        move = move - 1                         # change from (1, 9) to (0, 8)
        
        if not (0 <= move <= 8) or board[move] != ' ': # not in range or filled
            print("Invalid move. Please choose an empty cell between 1 and 9.")
            continue

        board[move] = current_player          # save move by player in board

        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw():
            print_board()
            print("It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            # swap 'X' with 'O' (and vice versa)


play_game()


"""
Example output:

 -------------
 |   |   |   |
 -------------
 |   |   |   |
 -------------
 |   |   |   |
 -------------
Player X, enter your move (1-9): 1

 -------------
 | X |   |   |
 -------------
 |   |   |   |
 -------------
 |   |   |   |
 -------------
Player O, enter your move (1-9): 2

 -------------
 | X | O |   |
 -------------
 |   |   |   |
 -------------
 |   |   |   |
 -------------
Player X, enter your move (1-9): 3

 -------------
 | X | O | X |
 -------------
 |   |   |   |
 -------------
 |   |   |   |
 -------------
Player O, enter your move (1-9): 4

 -------------
 | X | O | X |
 -------------
 | O |   |   |
 -------------
 |   |   |   |
 -------------
Player X, enter your move (1-9): 5

 -------------
 | X | O | X |
 -------------
 | O | X |   |
 -------------
 |   |   |   |
 -------------
Player O, enter your move (1-9): 6

 -------------
 | X | O | X |
 -------------
 | O | X | O |
 -------------
 |   |   |   |
 -------------
Player X, enter your move (1-9): 7

 -------------
 | X | O | X |
 -------------
 | O | X | O |
 -------------
 | X |   |   |
 -------------
Player X wins!    
"""

"""
Example output:

 -------------
 |   |   |   |
 -------------
 |   |   |   |
 -------------
 |   |   |   |
 -------------
Player X, enter your move (1-9): 1

 -------------
 | X |   |   |
 -------------
 |   |   |   |
 -------------
 |   |   |   |
 -------------
Player O, enter your move (1-9): 5

 -------------
 | X |   |   |
 -------------
 |   | O |   |
 -------------
 |   |   |   |
 -------------
Player X, enter your move (1-9): 7

 -------------
 | X |   |   |
 -------------
 |   | O |   |
 -------------
 | X |   |   |
 -------------
Player O, enter your move (1-9): 4

 -------------
 | X |   |   |
 -------------
 | O | O |   |
 -------------
 | X |   |   |
 -------------
Player X, enter your move (1-9): 6

 -------------
 | X |   |   |
 -------------
 | O | O | X |
 -------------
 | X |   |   |
 -------------
Player O, enter your move (1-9): 2

 -------------
 | X | O |   |
 -------------
 | O | O | X |
 -------------
 | X |   |   |
 -------------
Player X, enter your move (1-9): 8

 -------------
 | X | O |   |
 -------------
 | O | O | X |
 -------------
 | X | X |   |
 -------------
Player O, enter your move (1-9): 9

 -------------
 | X | O |   |
 -------------
 | O | O | X |
 -------------
 | X | X | O |
 -------------
Player X, enter your move (1-9): 3

 -------------
 | X | O | X |
 -------------
 | O | O | X |
 -------------
 | X | X | O |
 -------------
It's a draw!    
"""