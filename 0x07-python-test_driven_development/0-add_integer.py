#!/usr/bin/python3
"""testing module



"""


def add_integer(a, b=98):
    """this function retuns the sum of a and b
    and checks if a and b are integer or float
    """
    if (not isinstance(a, int) and
       not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and
       not isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)