import math

# Create empty board
board = [' ' for _ in range(9)]

# Function to display the board
def print_board():
    print()
    for i in range(3):
        print(board[i * 3] + " | " + board[i * 3 + 1] + " | " + board[i * 3 + 2])
        if i < 2:
            print("--+---+--")
    print()

# Function to check winner
def check_winner(player):
    win_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in win_positions:
        if all(board[i] == player for i in position):
            return True

    return False

# Function to check draw
def is_draw():
    return ' ' not in board

# Minimax Algorithm
def minimax(is_maximizing):

    if check_winner('O'):
        return 1

    if check_winner('X'):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)

        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'O'

# Human Move
def human_move():

    while True:
        move = int(input("Enter position (1-9): ")) - 1

        if 0 <= move <= 8 and board[move] == ' ':
            board[move] = 'X'
            break

        else:
            print("Invalid move! Try again.")

# Main Program
print("================================")
print("       TIC-TAC-TOE AI")
print("================================")
print("You are X")
print("AI is O")

print_board()

while True:

    # Human Turn
    human_move()
    print_board()

    if check_winner('X'):
        print("Congratulations! You win!")
        break

    if is_draw():
        print("Match Draw!")
        break

    # AI Turn
    print("AI is making a move...")
    ai_move()
    print_board()

    if check_winner('O'):
        print("AI wins!")
        break

    if is_draw():
        print("Match Draw!")
        break