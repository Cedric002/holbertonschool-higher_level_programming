#!/usr/bin/python3
"""Define a square.
"""


class Square:
    """class Square with a private instance attribute size,
    a instantiation with optinal and Public instance
    that returns the current square area.
    The size must be an integer and more than 0.
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size ** 2
