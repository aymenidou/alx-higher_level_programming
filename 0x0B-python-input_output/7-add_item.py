#!/usr/bin/python3
"""module for 0x0B-python-input_output"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    obj = load_from_json_file("add_item.json")
except Exception:
    save_to_json_file([], "add_item.json")
obj = load_from_json_file("add_item.json")
list = []
for i in range(1, len(sys.argv)):
    list.append(sys.argv[i])
obj = obj + list
save_to_json_file(obj, "add_item.json")
