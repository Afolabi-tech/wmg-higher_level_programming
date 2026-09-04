#!/usr/bin/python3
"""
0-nqueens.py

This program solves the N queens problem: placing N
non-attacking queens on an NxN chessboard, and prints every
possible solution.

Usage: nqueens N
"""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at (row, col) safely.

    Args:
        board (list): The current placement, board[i] is the
            column of the queen placed in row i (for rows < row).
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if placing a queen at (row, col) is safe.
    """
    for prev_row in range(row):
        prev_col = board[prev_row]
        if prev_col == col:
            return False
        if abs(prev_col - col) == abs(prev_row - row):
            return False
    return True


def solve(n, row, board, solutions):
    """Recursively try to place queens row by row (backtracking).

    Args:
        n (int): The size of the board.
        row (int): The current row to place a queen in.
        board (list): The current placement so far.
        solutions (list): Accumulator for all valid solutions found.
    """
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve(n, row + 1, board, solutions)
            board.pop()


def print_solution(board):
    """Print a single solution as a list of [row, column] pairs.

    Args:
        board (list): board[i] is the column of the queen in row i.
    """
    coords = [[row, col] for row, col in enumerate(board)]
    print(coords)


def main():
    """Parse arguments, validate them, and solve the N queens puzzle."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve(n, 0, [], solutions)

    for board in solutions:
        print_solution(board)


if __name__ == "__main__":
    main()
