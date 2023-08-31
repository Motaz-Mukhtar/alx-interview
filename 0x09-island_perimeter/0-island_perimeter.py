#!/usr/bin/python3
"""
    Island Perimeter.
"""


def island_perimeter(grid):
    """
        Returns the perimeter of the
        island described in 'grid'.
    """
    perimeter = 0
    size = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                size += 1
                if grid[row][col - 1] == 1:
                    perimeter += 1
                if grid[row - 1][col] == 1:
                    perimeter += 1

    return size * 4 - perimeter * 2
