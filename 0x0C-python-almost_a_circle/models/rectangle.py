#!/usr/bin/python3
"""0x0C. Python - Almost a circle Python OOP"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        self.__width = value

    @height.setter
    def height(self, value):
        """set value of height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """set value of x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """set value of y"""
        self.__y = value
