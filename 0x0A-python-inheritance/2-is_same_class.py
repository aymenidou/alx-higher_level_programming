#!/usr/bin/python3
"""module containing comparator function"""


def is_same_class(obj, a_class):
    """method to check if an object is
    an instance of the class"""
    return type(obj) is a_class
