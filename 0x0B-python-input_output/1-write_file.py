#!/usr/bin/python3
"""module for 0x0B-python-input_output"""


def write_file(filename="", text=""):
    """write_file"""
    with open(filename, 'w') as f:
        wr = f.write(text)
    return wr
