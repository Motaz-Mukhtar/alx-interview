#!/usr/bin/python3
"""
    Solve n_queens Problem, using backtrack Algorithm.
"""
from typing import List
import sys


results = []

try:
    N = int(sys.argv[1])
except IndexError:
    print("Usage: nqueens N")
    sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)


def accept(board: List[List], row: int, col: int) -> bool:
    """
        Return True if the queen is safe,
        else return false.
    """

    for y in range(col):
        if board[row][y]:
            return False

    x = row
    y = col

    # Check left upper diagonal
    while x >= 0 and y >= 0:
        if board[x][y]:
            return False

        x -= 1
        y -= 1

    x = row
    y = col

    # Check left lower diagonal
    while y >= 0 and x < N:
        if board[x][y]:
            return False

        x += 1
        y -= 1

    return True


def n_queens(board: List[List], col: int) -> bool:
    """
        Find all possible solutions for N queens
        problem, in N*N board..
    """
    # if the loop reach the end of the board.
    if col == N:
        result = []
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == 1:
                    result.append([x, y])
        results.append(result)
        return True

    res = False
    for row in range(N):
        # check if the queen are safe.
        if accept(board, row, col):
            board[row][col] = 1

            res = n_queens(board, col + 1) or res

            board[row][col] = 0

    return res


def main(n: int) -> List[List]:
    """
        Create N*N chess board and
        run n_queens() function, and
        return the possible solutions.
    """
    board = [[0 for y in range(N)]
             for x in range(N)]

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    n_queens(board, 0)
    results.sort()
    return results


all_solutions = main(N)


for solution in all_solutions:
    print(solution)
