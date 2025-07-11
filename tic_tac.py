import math

def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def is_winner(board, player):
    win_states = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player]*3 in win_states

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if is_winner(board, "O"):
        return 1
    elif is_winner(board, "X"):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("You are 'X', AI is 'O'")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell already taken. Try again.")
            except:
                print("Invalid input. Try again.")
        print_board(board)

        if is_winner(board, "X"):
            print("You win! ")
            break
        elif is_board_full(board):
            print("It's a tie! ")
            break

        # AI move
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        print("AI played:")
        print_board(board)

        if is_winner(board, "O"):
            print("AI wins! ")
            break
        elif is_board_full(board):
            print("It's a tie! ")
            break

if __name__ == "__main__":
    play_game()
