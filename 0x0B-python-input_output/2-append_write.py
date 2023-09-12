#!/usr/bin/python3
"""module for 0x0B-python-input_output"""


def append_write(filename="", text=""):
    """append_write"""
    with open(filename, 'a') as f:
        wr = f.write(text)
    return wr
