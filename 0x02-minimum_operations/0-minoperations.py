#!/usr/bin/python3
"""
    Minimum Operations
"""


def minOperations(n: int) -> int:
    """
        Calculates the fewest number of
        operations needed to result in
        exactly n H Characters in the file.
    """
    text_list = ['H']
    copy_list = []
    number_of_operations = 0

    if n <= 0:
        return 0

    if n == 1:
        return 0

    if n == 2:
        return 2

    if n == 3:
        return 3

    num = 0
    while True:
        # Even
        # if even just Paste
        if n % len(text_list) == 0:
            copy_list = text_list.copy()
            for i in copy_list:
                text_list.append(i)
            number_of_operations += 2
        # Odd
        # if odd Copy, and Paste
        else:
            for i in copy_list:
                text_list.append(i)
            number_of_operations += 1

        if n / 2 == len(text_list):
            copy_list = text_list.copy()
            for i in copy_list:
                text_list.append(i)
            number_of_operations += 2

        if len(text_list) == n:
            return number_of_operations
        num += 1
    return number_of_operations
