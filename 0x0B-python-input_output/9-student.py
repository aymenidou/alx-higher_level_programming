#!/usr/bin/python3
"""module for 0x0B-python-input_output"""



class Student:
    """Public instance attributes:
    first_name
    last_name
    age"""
    def __init__(self, first_name, last_name, age):
        """init object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance """
        return self.__dict__
