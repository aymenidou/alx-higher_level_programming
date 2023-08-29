#!/usr/bin/python3
"""Class Square"""


class Square:
    """empty class Square that defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialization method
        """
        self.size = size
        self.position = position

    def area(self):
        """Area method
        """
        return self.__size * self.__size

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """retrieve position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
           len(value) != 2 or
           not isinstance(value[0], int) or
           not isinstance(value[1], int) or
           value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """print square"""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
