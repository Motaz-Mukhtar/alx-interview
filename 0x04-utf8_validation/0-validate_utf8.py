#!/usr/bin/python3
"""
    UTF-8 Validation
"""
to_binary = __import__('convert_to_binary').to_binary


def validUTF8(data):
    """
        Determines if a given data set represents
        a valid UTF-8 encoding, True if data is
        valid UTF-8 ending, else return False
    """
    binary_data = [to_binary(i) for i in data]
    for binary_list in binary_data:
        for index in range(len(binary_list)):
            if binary_list[0] == 0:
                continue
            elif (binary_list[0] == 1 and
                  binary_list[1] == 0):
                continue
            elif (binary_list[0] == 1 and
                  binary_list[1] == 1 and
                  binary_list[2] == 0):
                continue
            elif (binary_list[0] == 1 and
                  binary_list[1] == 1 and
                  binary_list[2] == 1 and
                  binary_list[3] == 0):
                continue
            elif (binary_list[0] == 1 and
                  binary_list[1] == 1 and
                  binary_list[2] == 1 and
                  binary_list[3] == 1 and
                  binary_list[4] == 0):
                continue
            else:
                return False
    return True
