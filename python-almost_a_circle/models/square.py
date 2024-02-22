#!/usr/bin/python3
"""
Define a class Square.
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Classe Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size, size)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )
