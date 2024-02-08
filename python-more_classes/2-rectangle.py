#!/usr/bin/python3
"""
Define a square
"""


class Rectangle:
    """
    class Square with a private instance attribute width,
    a property def width(self),
    a property setter def width(self, value): width must be an integer,
    otherwise TypeError "width must be an integer".
    If width < 0, ValueError "width must be >= 0".
    a private instance attribute height,
    a property def height(self),
    a property setter def height(self, value)
    and a instantiation with optional width and height:
    a public instance method: def area(self): that returns the rectangle area
    Public instance method: def perimeter(self): that returns the rectangle
    perimeter: def __init__(self, width=0, height=0)
    """

    class Rectangle:
        def __init__(self, width=0, height=0):
            self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._width ==0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)
