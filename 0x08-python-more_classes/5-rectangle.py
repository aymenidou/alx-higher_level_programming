#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """defining rectangle"""

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set value of width"""
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value of height"""
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """init method"""
        self.height = height
        self.width = width

    def area(self):
        """area method"""
        return self.height * self.width

    def perimeter(self):
        """perimeter method"""
        if (self.width == 0 or self.height == 0):
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """print rectangle"""
        rect = ""
        if (self.width == 0 or self.height == 0):
            return rect
        else:
            for i in range(self.height):
                for j in range(self.width):
                    rect += '#'
                if (i == self.height - 1):
                    return rect
                rect += "\n"

    def __repr__(self):
        """rectangle representation"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """rectangle deletion"""
        print("Bye rectangle...")
