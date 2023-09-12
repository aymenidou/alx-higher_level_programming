#!/usr/bin/python3
"""module for 0x0B-python-input_output"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file"""
    with open(filename, 'w') as f:
        j = json.dumps(my_obj)
        f.write(j)
