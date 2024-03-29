#!/usr/bin/python3
"""0x0C. Python - Almost a circle Python OOP"""
import json
import csv
from turtle import *


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
            return []
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes attributes of list_objs to a csv file"""
        with open(cls.__name__ + ".csv", "w") as f:
            cwriter = csv.writer(f, delimiter=',')
            for obj in list_objs:
                my_l = []
                if cls.__name__ == "Rectangle":
                    my_l.append(obj.id)
                    my_l.append(obj.width)
                    my_l.append(obj.height)
                    my_l.append(obj.x)
                    my_l.append(obj.y)
                elif cls.__name__ == "Square":
                    my_l.append(obj.id)
                    my_l.append(obj.size)
                    my_l.append(obj.x)
                    my_l.append(obj.y)
                cwriter.writerow(my_l)

    @classmethod
    def load_from_file_csv(cls):
        """
        reads a csv file and returns the list of instances
        that exist in the file
        """
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                rs = csv.reader(f, delimiter=',')
                ls = []
                if cls.__name__ == "Rectangle":
                    for i in rs:
                        row = cls(
                                int(i[1]),
                                int(i[2]),
                                int(i[3]),
                                int(i[4]),
                                int(i[0])
                                )
                        ls.append(row)
                    return ls
                elif cls.__name__ == "Square":
                    for i in rs:
                        row = cls(int(i[1]), int(i[2]), int(i[3]), int(i[0]))
                        ls.append(row)
                    return ls
        except Exception:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        bgcolor(0, 0, 0)
        color(1, 1, 1)
        pensize(2)
        i = 0
        for rect in list_rectangles:
            forward(rect.width)
            right(90)
            forward(rect.height)
            right(90)
            forward(rect.width)
            right(90)
            forward(rect.height)
            penup()
            i += rect.width + 10
            setposition(i, 0)
            pendown()
            right(90)

        for square in list_squares:
            forward(square.size)
            right(90)
            forward(square.size)
            right(90)
            forward(square.size)
            right(90)
            forward(square.size)
            penup()
            i += square.size + 10
            setposition(i, 0)
            pendown()
            right(90)
        exitonclick()
