#!/usr/bin/python3
"""testing module



"""


def add_integer(a, b=98):
    """this function retuns the sum of a and b
    and checks if a and b are integer or float
    """
    if (type(a) is not int and
       type(a) is not float):
        raise TypeError("a must be an integer")
    
    if (type(b) is not int and
       type(b) is not float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)