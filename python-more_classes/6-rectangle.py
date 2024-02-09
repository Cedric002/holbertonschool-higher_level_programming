#!/usr/bin/python3
"""
Define a rectangle
"""


class Rectangle:
    """
    class Rectangle with a private instance attribute width,
    a property def width(self),
    a property setter def width(self, value): width must be an integer,
    otherwise TypeError "width must be an integer".
    If width < 0, ValueError "width must be >= 0".
    a private instance attribute height,
    a property def height(self),
    a property setter def height(self, value): height must be an integer,
    otherwise TypeError "height must be an integer".
    If height < 0, ValueError "height must be >= 0".
    Public class attribute number_of_instances: initialized to 0,
    incremented during each new instance instantiation and
    decremented during each instance deletion.
    Instantiation with optional width and height:
    def __init__(self, width=0, height=0):
    a public instance method: def area(self): returns the rectangle area,
    a public instance method: def perimeter(self): returns the rectangle
    perimeter: if width = 0 or height = 0, perimeter(self) = 0,
    print() and str() print the rectangle with the character #.
    If width = 0 or height = 0, return an empty string.
    repr() return string representation of the rectangle for to recreate a new
    instance by using eval().
    Print "Bye rectangle..." when an instance of Rectangle is deleted.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            return '#' * (self.__width * self.__height)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
