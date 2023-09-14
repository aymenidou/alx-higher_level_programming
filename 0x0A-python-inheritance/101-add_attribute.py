#!/usr/bin/python3
"""Can I?"""


def add_attribute(mc, name, value):
    """function that adds a new attribute to an object if it’s possible"""
    if (hasattr(mc, "__dict__")):
        raise TypeError("can't add new attribute")
    else:
        setattr(mc, name, value)
