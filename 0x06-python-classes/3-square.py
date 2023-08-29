#!/usr/bin/python3
"""Class Square"""


class Square:
    """empty class Square that defines a square
    """
    __size = None

    def __init__(self, size=0):
        """Initialization method
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        return self.__size ** self.__size
