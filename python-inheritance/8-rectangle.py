#!/usr/bin/python3
"""
The function print class Rectangle that inherits from BaseGeometry with
instantiation with width and height: def __init__(self, width, height):
width and height must be private and
width and height must be positive integers, validated by integer_validator
"""


class BaseGeometry:
    """
    The classe define a geometrie and have that inherits a rectangle
    """
    pass

def integer_validator(value, attribute_name):
    if not isinstance(value, int):
        raise TypeError(f"{attribute_name} must be an integer")
    elif value <= 0:
        raise ValueError("Value must be a positive integer")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        integer_validator(width, 'width')
        integer_validator(height, 'height')
        self.__width = width
        self.__height = height
