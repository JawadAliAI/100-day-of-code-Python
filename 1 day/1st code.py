import random

# Initialize the game board as a list of empty cells
board = [' ' for i in range(9)]

# Function to display the game board


def display_board():
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

# Function to check if a player has won


def check_win(player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))

# Function to check if the board is full


def check_board_full():
    return ' ' not in board

# Function for the AI to make a move


def ai_move():
    # Check if the AI can win in the next move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_win('O'):
                return
            else:
                board[i] = ' '

    # Check if the player can win in the next move and block them
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_win('X'):
                board[i] = 'O'
                return
            else:
                board[i] = ' '

    # Choose a random empty cell
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            board[move] = 'O'
            return

# Function to play the game


def play_game():
    print('Welcome to Tic Tac Toe!')
    display_board()

    while True:
        # Player's turn
        player_move = input('Enter your move (1-9): ')
        player_move = int(player_move) - 1

        if board[player_move] != ' ':
            print('That cell is already occupied. Try again.')
            continue
        else:
            board[player_move] = 'X'

        # Check for win or draw
        if check_win('X'):
            display_board()
            print('Congratulations! You win!')
            break
        elif check_board_full():
            display_board()
            print('The board is full. It\'s a draw!')
            break
            # AI's turn
    ai_move()

    # Check for win or draw
    if check_win('O'):
        display_board()
        print('Sorry, you lose. Better luck next time!')
    elif check_board_full():
        display_board()
        print('The board is full. It\'s a draw!')
    # Display the current board
    display_board()
