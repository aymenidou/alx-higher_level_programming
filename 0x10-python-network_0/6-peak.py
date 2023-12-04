#!/usr/bin/python3
"""this module contain find_peak function"""


def find_peak(list_of_integers):
    """find the peak in a list of integers"""
    if (len(list_of_integers) == 0):
        return None
    max = list_of_integers[0]
    for i in list_of_integers:
        if (i > max):
            max = i
    return max
