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
    Other public class attribute print_symbol: initialized to #,
    used as symbol for string representation and can be any type.
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
    Static method def bigger_or_equal(rect_1, rect_2):
    returns biggest rectangle based on the area.
    rect_1 must be an instance of Rectangle,
    otherwise TypeError "rect_1 must be an instance of Rectangle".
    rect_2 must be an instance of Rectangle,
    otherwise TypeError "rect_2 must be an instance of Rectangle".
    Returns rect_1 if rect_1 and rect_2 = area value
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        return '\n'.join([''.join([self.print_symbol for nb in range(self.__width)]) for nb in range(self.__height)])

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
