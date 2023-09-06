#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """defining rectangle"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
                    rect += (str(self.print_symbol))
                if (i == self.height - 1):
                    return rect
                rect += "\n"

    def __repr__(self):
        """rectangle representation"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """rectangle deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """function to return the biggest rect"""
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if (area_2 > area_1):
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """return a square"""
        if (not isinstance(size, int)):
            raise TypeError
        if (size < 0):
            raise ValueError
        return Rectangle(size, size)
