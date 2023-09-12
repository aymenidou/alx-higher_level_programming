#!/usr/bin/python3
"""module for 0x0B-python-input_output"""


def read_file(filename=""):
    """function that reads a text file (UTF8)
    and prints it to stdout"""
    # f = open(filename, 'w', encoding="utf-8")
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
    f.closed
