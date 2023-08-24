#!/usr/bin/python3
"""
    Making Change.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
    """
    if total < 0:
        return 0

    total_coins = sum(coins)

    n = total - total_coins

    if n < 0:
        return -1

    return n
