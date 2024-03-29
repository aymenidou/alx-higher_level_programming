#!/usr/bin/python3
"""print_square module
"""


def print_square(size):
    """function that print a square"""
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (not isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
