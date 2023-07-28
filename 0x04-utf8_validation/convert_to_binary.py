#!/usr/bin/python3
"""
    Create to_binary() function
"""
import math


def to_binary(num: int):
    binary_list = []

    while num != 0:
        if num % 2 == 0:
            binary_list.append(0)
        else:
            binary_list.append(1)
        num = math.trunc(num / 2)

    binary_list.reverse()
    return binary_list
