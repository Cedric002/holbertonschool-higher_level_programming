#!/usr/bin/python3
"""Define a square.
"""


class Square:
    """class Square with a private instance attribute size and a instantiation with optinal.
    The size should be an integer and more than 0.
    """

    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size
