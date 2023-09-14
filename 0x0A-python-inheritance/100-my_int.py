#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """class MyInt that inherits from int"""
    def __eq__(self, __value: object):
        """function reverse equal"""
        return self.real != __value

    def __ne__(self, __value: object):
        """function reverse not equal"""
        return self.real == __value
