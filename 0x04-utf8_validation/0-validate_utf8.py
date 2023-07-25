#!/usr/bin/python3
"""
    UTF-8 Validation
"""


def validUTF8(data):
    """
        Determines if a given data set represents
        a valid UTF-8 encoding, True if data is
        valid UTF-8 ending, else return False
    """
    for num in data:
        bin_num = bin(num)
        if len(bin_num[2:]) > 8:
            return False
    return True
