#!/usr/bin/python3
"""0x0C. Python - Almost a circle Python OOP"""
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if (list_dictionaries is None):
            return "[]"
        return json.dumps(list_dictionaries)
