#!/usr/bin/python3
"""
The function print class Rectangle that inherits from BaseGeometry with
instantiation with width and height: def __init__(self, width, height):
width and height must be private and
width and height must be positive integers, validated by integer_validator
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Use from 7-base_geometry.py for the inherits of Rectangle
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
