#!/usr/bin/python3
"""
Define a square
"""


class Rectangle:
    """
    class Square with a private instance attribute width,
    a property def width(self),
    a property setter def width(self, value),
    a private instance attribute height,
    a property def height(self),
    a property setter def height(self, value)
    and a instantiation with optional width and height:
    def __init__(self, width=0, height=0)
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=  0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=  0")
        else:
            self.__height = value
