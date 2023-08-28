#!/usr/bin/python3
"""
    Island Perimeter.
"""


def incr_perimeter(grid, row, col):
    """
        Check horizontally/vertically for water
        and increses perimeter.
    """
    perimeter = 0

    try:
        if grid[row][col + 1] == 0:
            perimeter += 1
    except KeyError:
        pass

    try:
        if grid[row][col - 1] == 0:
            perimeter += 1
    except KeyError:
        pass

    try:
        if grid[row + 1][col] == 0:
            perimeter += 1
    except KeyError:
        pass

    try:
        if grid[row - 1][col] == 0:
            perimeter += 1
    except KeyError:
        pass

    return perimeter

def island_perimeter(grid):
    """
        Returns the perimeter of the
        island described in 'grid'.
    """
    perimeter = 0

    for row in range(len(grid)):
        if 1 not in grid[row]:
            continue

        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter += incr_perimeter(grid, row, col)

    return perimeter
