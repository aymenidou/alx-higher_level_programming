#!/usr/bin/python3
"""0x0C. Python - Almost a circle Python OOP"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """return width"""
        return self.__width

    @property
    def height(self):
        """return height"""
        return self.__height

    @property
    def x(self):
        """return x"""
        return self.__x

    @property
    def y(self):
        """return y"""
        return self.__y

    @width.setter
    def width(self, value):
        """set value of width"""
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set value of height"""
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """set value of x"""
        if (not isinstance(value, int)):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """set value of y"""
        if (not isinstance(value, int)):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return rectangle area"""
        return self.width * self.height

    def display(self):
        """print rectangle to stdout"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """return rectangle info"""
        str = "[Rectangle]"
        str += " ({}) {}/{} ".format(self.id, self.x, self.y)
        str += " - {}/{}".format(self.width, self.height)
        return str
