#!/usr/bin/python3
"""0x0C. Python - Almost a circle Python OOP"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialisation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """display square info"""
        str = "[Square]"
        str += " ({}) {}/{} ".format(self.id, self.x, self.y)
        str += " - {}".format(self.width)
        return str
