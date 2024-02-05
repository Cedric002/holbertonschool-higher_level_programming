#!/usr/bin/python3
"""Define a square.
"""


class Square:
    """class Square with a private instance attribute size,
    a property def size(self), a property setter def size(self, value)
    and a public instance method: def area(self).
    The size must be an integer and more than 0.
    """

    def __init__(self, size=0):
        self.__size = size

    def size(self):
        """
        Property
        """
        return self.__size

    def size(self, value):
        """
        Property setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size ** 2
