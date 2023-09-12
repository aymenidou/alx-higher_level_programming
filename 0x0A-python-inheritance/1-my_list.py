#!/usr/bin/python3
"""
module containing class MyList
"""


class MyList(list):
    """Class MyList"""
    def print_sorted(self):
        """method return sorted list"""
        print(sorted(self))
