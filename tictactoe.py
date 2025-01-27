# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if the current player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True

    if all([board[i][i] == player for i in range(3)]):  # Check diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Check reverse diagonal
        return True

    return False

# Function to check if the board is full
def is_full(board):
    return all([cell != " " for row in board for cell in row])

# Main function to run the game
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize the board
    current_player = "X"  # X always goes first

    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Player {current_player}, enter your move (row col): ").split())
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid move. Try again.")
            continue
        
        board[row][col] = current_player  # Place the player's move

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
tic_tac_toe()
