#!/usr/bin/python3
"""
    Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
        Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    copy = matrix.copy()
    col = 0

    while col < len(matrix):
        row = len(matrix) - 1
        temp = []
        while row >= 0:
            temp.append(copy[row][col])
            row -= 1

        matrix[col] = temp
        print(temp)
        col += 1
