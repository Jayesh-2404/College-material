import math

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_moves_left(board):
    """Checks if there are any moves left on the board."""
    for row in board:
        if ' ' in row:
            return True
    return False

def evaluate(board):
    """Evaluates the board and returns a score for terminal states."""
    # Check rows for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            if row[0] == 'X':
                return 10
            elif row[0] == 'O':
                return -10

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    # If no one has won yet
    return 0

def minimax(board, depth, is_max):
    """Implements the Minimax algorithm."""
    score = evaluate(board)

    # If Maximizer has won
    if score == 10:
        return score - depth

    # If Minimizer has won
    if score == -10:
        return score + depth

    # If no moves left, it's a draw
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ' '
        return best

def find_best_move(board, is_max):
    """Finds the best move for the current player."""
    if is_max:
        best_val = -math.inf
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    move_val = minimax(board, 0, False)
                    board[i][j] = ' '

                    if move_val > best_val:
                        best_val = move_val
                        best_move = (i, j)
    else:
        best_val = math.inf
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    move_val = minimax(board, 0, True)
                    board[i][j] = ' '

                    if move_val < best_val:
                        best_val = move_val
                        best_move = (i, j)

    return best_move

# Game loop for two players
if __name__ == "__main__":
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True  # True for Player X, False for Player O

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while is_moves_left(board) and evaluate(board) == 0:
        if player_turn:
            print("Player X's turn")
        else:
            print("Player O's turn")

        best_move = find_best_move(board, player_turn)
        print(f"Suggested move: Row {best_move[0]}, Column {best_move[1]}")

        while True:
            try:
                row = int(input("Enter the row (0, 1, 2): "))
                col = int(input("Enter the column (0, 1, 2): "))

                if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
                    print("Invalid move. Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        board[row][col] = 'X' if player_turn else 'O'
        print_board(board)

        if evaluate(board) != 0:
            break

        player_turn = not player_turn

    result = evaluate(board)
    if result == 10:
        print("Player X wins!")
    elif result == -10:
        print("Player O wins!")
    else:
        print("It's a draw!")
