#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """
        returns a list of lists of
        integers representing the
        Pascals triangle of n.
    """

    triangle_list = ['1']
    main_list = []
    copy_list = []

    main_list.append(triangle_list.copy())
    if n <= 0:
        return main_list

    for i in range(n - 1):
        triangle_list.append('0')
        copy_list = triangle_list.copy()
        copy_list.reverse()

        for index in range(len(triangle_list)):
            triangle_list[index] =\
             str(int(triangle_list[index]) + int(copy_list[index]))

        main_list.append(triangle_list.copy())

    return main_list
