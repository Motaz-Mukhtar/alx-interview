#!/usr/bin/python3
"""
    Create to_binary() function
"""
import math


def to_binary(num: int):
    binary_list = [0, 0, 0, 0, 0, 0, 0, 0]
    length = len(binary_list) - 1

    while num != 0:
        if num % 2 == 0:
            pass
        else:
            binary_list[length] = 1
        num = math.trunc(num / 2)
        length -= 1

    while len(binary_list) < 8:
        binary_list.append(0)

    binary_list.reverse()
    return binary_list
