#!/usr/bin/python3
"""module conatining empty class"""


class BaseGeometry:
    """class BaseGeometry with one function
    """
    def area(self):
        """function raising an exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validate in integer"""
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
