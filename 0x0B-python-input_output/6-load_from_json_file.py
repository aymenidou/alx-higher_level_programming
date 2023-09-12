#!/usr/bin/python3
"""module for 0x0B-python-input_output"""
import json


def load_from_json_file(filename):
    """load_from_json_file"""
    with open(filename, 'r') as f:
        data = f.read()
        return json.loads(data)
