def print_board(board):
    print("  0 1 2")
    for row, line in enumerate(board):
        print(f"{row} {' '.join(line)}")


def check_winner(board):
    lines = [
        # Horizontal
        board[0], board[1], board[2],
        # Vertical
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    
    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != " ":
            return line[0]
    
    return None


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves = 0

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0-2): "))
        col = int(input(f"Player {current_player}, enter the column (0-2): "))

        if board[row][col] != " ":
            print("This position is already taken. Try again.")
            continue

        board[row][col] = current_player
        moves += 1

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if moves == 9:
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
