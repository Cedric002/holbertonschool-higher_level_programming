#!/usr/bin/python3
"""
The function print class Rectangle that inherits from BaseGeometry with
instantiation with width and height: def __init__(self, width, height):
width and height must be private and
width and height must be positive integers, validated by integer_validator
area() method must be implemented and
print() should print, and str() should return: [Rectangle] <width>/<height>
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Use from 7-base_geometry.py for the inherits of Rectangle
    """
    def __init__(self, width, height):
        try:
            self.__width = int(width)
            self.__height = int(height)
        except ValueError:
            raise ValueError("Width and height must be integers.")
        if self.__width <= 0 or self.__height <= 0:
            raise ValueError("Width and height must be positive integers.")

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
