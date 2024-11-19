import math

# Define the player types
PLAYER = "X"
OPPONENT = "O"

# Check if there are moves left on the board
def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

# Evaluate the board for a win, loss, or draw
def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return 10 if row[0] == PLAYER else -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return 10 if board[0][col] == PLAYER else -10
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 10 if board[0][0] == PLAYER else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 10 if board[0][2] == PLAYER else -10
    return 0

# Minimax function
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    
    # Return the score if someone wins or it's a draw
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0
    
    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = PLAYER
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = OPPONENT
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

# Find the best move for the player
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = PLAYER
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

# Example usage
board = [
    ["X", "O", "X"],
    ["O", "O", " "],
    ["X", " ", " "]
]

best_move = find_best_move(board)
print(f"The best move is at position: {best_move}")
