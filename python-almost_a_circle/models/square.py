#!/usr/bin/python3
"""
Define a class Square.
Update: adding the public getter and setter size.
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Classe Square that inherits from Rectangle.
    The setter assign width and height.
    The setter have the same value validation as
    the Rectangle for width and height.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size, size)i

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.set_width(value)
        self.set_height(value)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )
