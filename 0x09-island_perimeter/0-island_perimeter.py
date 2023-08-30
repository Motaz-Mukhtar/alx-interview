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

    if row == 0:
        # Right Check
        try:
            if grid[row][col + 1] == 0:
                perimeter += 1
        except IndexError:
            pass

        # Bottom Check
        if grid[row + 1][col] == 0:
            perimeter += 1

        return perimeter

    if col == 0:
        # Right Check
        if grid[row][col + 1] == 0:
            perimeter += 1

        # Bottom Check
        try:
            if grid[row + 1][col] == 0:
                perimeter += 1
        except IndexError:
            pass

        return perimeter

    try:
        # Right Check
        if grid[row][col + 1] == 0:
            perimeter += 1
    except IndexError:
        pass

    try:
        # Left Check
        if grid[row][col - 1] == 0:
            perimeter += 1
    except IndexError:
        pass

    try:
        # Bottom Check
        if grid[row + 1][col] == 0:
            perimeter += 1
    except IndexError:
        pass

    try:
        # Top Check
        if grid[row - 1][col] == 0:
            perimeter += 1
    except IndexError:
        pass

    return perimeter


def island_perimeter(grid):
    """
        Returns the perimeter of the
        island described in 'grid'.
    """
    perimeters = 0

    for row in range(len(grid)):
        if 1 not in grid[row]:
            continue

        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeters += incr_perimeter(grid, row, col)

    return perimeters
