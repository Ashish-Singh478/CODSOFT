import math

board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("-" * 9)

def is_empty(r, c):
    return board[r][c] == " "

def is_full():
    return all(cell != " " for row in board for cell in row)

def check_winner(brd, player):
    for i in range(3):
        if all(brd[i][j] == player for j in range(3)) or all(brd[j][i] == player for j in range(3)):
            return True
    if brd[0][0] == brd[1][1] == brd[2][2] == player:
        return True
    if brd[0][2] == brd[1][1] == brd[2][0] == player:
        return True
    return False

def get_moves(brd):
    return [(r, c) for r in range(3) for c in range(3) if brd[r][c] == " "]

def minimax(brd, is_maximizing):
    if check_winner(brd, "O"):
        return 1
    elif check_winner(brd, "X"):
        return -1
    elif is_full():
        return 0

    if is_maximizing:
        best = -math.inf
        for r, c in get_moves(brd):
            brd[r][c] = "O"
            score = minimax(brd, False)
            brd[r][c] = " "
            best = max(best, score)
        return best
    else:
        best = math.inf
        for r, c in get_moves(brd):
            brd[r][c] = "X"
            score = minimax(brd, True)
            brd[r][c] = " "
            best = min(best, score)
        return best

def ai_move():
    best_score = -math.inf
    move = None
    for r, c in get_moves(board):
        board[r][c] = "O"
        score = minimax(board, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            move = (r, c)
    board[move[0]][move[1]] = "O"

def main():
    print("Let's play Tic Tac Toe!")
    print("You will use 'X' and the computer will use 'O'.")
    print("Valid Entries: 0 0, 0 1, 0 2, 1 0, 1 1, 1 2, 2 0, 2 1, 2 2\n")
    print_board()

    while True:
        try:
            move = input("\nEnter your move (row and column, e.g., '1 2'): ")
            r, c = map(int, move.split())
        except:
            print("❌ Invalid input. Try format like '1 2'")
            continue

        if r not in range(3) or c not in range(3):
            print("❌ Row and Column must be 0, 1, or 2.")
            continue
        if not is_empty(r, c):
            print("❌ That spot is already taken.")
            continue

        board[r][c] = "X"
        print_board()

        if check_winner(board, "X"):
            print("🎉 You win!")
            break
        if is_full():
            print("It's a tie!")
            break

        print("\nAI's move:")
        ai_move()
        print_board()

        if check_winner(board, "O"):
            print("💻 AI wins! Better luck next time.")
            break
        if is_full():
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()