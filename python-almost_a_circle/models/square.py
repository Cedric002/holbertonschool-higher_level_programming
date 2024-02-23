#!/usr/bin/python3
"""
Define a class Square.
Update: adding the public getter and setter size.
Update: adding the public method def update(self, *args, **kwargs)
Update: adding the public method def to_dictionary(self)
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
        super().__init__(id, x, y, size, size)

    def update(self, *args, **kwargs):
        """
        Public method assigns attributes:
        *args -> list of arguments (no-keyworded arguments) with
        1st argument -> id attribute
        2nd argument -> size attribute
        3rd argument -> x attribute
        4th argument -> y attribute
        **kwargs -> double pointer to a dictionary
        if *args exists and not empty, **kwargs must be skipped.
        """
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

    def to_dictionary(self):
        """
        Public method returns the dictionary representation of a Square
        """
        return {key: value for key, value in self.__dict__.items()
                if key in ['id', 'size', 'x', 'y']}

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )
