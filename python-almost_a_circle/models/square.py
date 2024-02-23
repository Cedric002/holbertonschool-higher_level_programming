#!/usr/bin/python3
"""
Define a class Square.
Update: adding the public getter and setter size.
Update: adding the public method def update(self, *args, **kwargs)
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Classe Square that inherits from Rectangle.
    The setter assign width and height.
    The setter have the same value validation as
    the Rectangle for width and height.
    The public method assigns attributes:
    *args -> list of arguments (no-keyworded arguments) with
    1st argument should be the id attribute
    2nd argument should be the size attribute
    3rd argument should be the x attribute
    4th argument should be the y attribute
    **kwargs -> double pointer to a dictionary: key/value (keyworded arguments)
    **kwargs must be skipped if *args exists and not empty
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size, size)

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )
