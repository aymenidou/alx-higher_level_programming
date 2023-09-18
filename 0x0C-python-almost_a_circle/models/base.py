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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if (list_dictionaries is None):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        array = []
        if (list_objs is not None):
            for obj in list_objs:
                array.append(obj.to_dictionary())
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(cls.to_json_string(array))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if (json_string is None):
            return ""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if (cls.__name__ == "Rectangle"):
            obj = cls(1, 1)
        elif (cls.__name__ == "Square"):
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                ls = cls.from_json_string(f.read())
                array = []
                for vals in ls:
                    array.append(cls.create(**vals))
                return array
        except Exception:
            return []
