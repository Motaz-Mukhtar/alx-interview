#!/usr/bin/python3
"""
    Making Change.
"""
import math


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
    """
    n = 0
    coins.sort(reverse=True)
    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            n += math.trunc(total / coin)
            total %= coin

    if total == 0:
        return n

    return -1
