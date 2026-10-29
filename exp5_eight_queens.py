"""Experiment 5 - 8-Queens using Recursive Backtracking"""

N = 8
attempts = 0   # number of placement attempts (every time a queen is tried on a square)


def is_safe(board, row, col):
    """Constraint check: no queen in same column or either diagonal of earlier rows."""
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(board, row=0):
    global attempts
    if row == N:                      # all queens placed -> goal
        return True
    for col in range(N):
        attempts += 1
        if is_safe(board, row, col):
            board[row] = col          # place queen
            if solve(board, row + 1):
                return True
            board[row] = -1           # backtrack: undo placement
    return False


def print_board(board):
    for r in range(N):
        print(" ".join("Q" if board[r] == c else "." for c in range(N)))


if __name__ == "__main__":
    board = [-1] * N                  # board[row] = column of queen in that row
    if solve(board):
        print("Final 8x8 board:\n")
        print_board(board)
        print("\nQueen positions (row, col), 1-indexed:")
        print([(r + 1, c + 1) for r, c in enumerate(board)])
        print("Placement attempts:", attempts)
    else:
        print("No solution found.")
