#!/usr/bin/python3
"""
The function print class Square that inherits from Rectangle with
instantiation with size: def __init__(self, size): .
size must be private. No getter or setter,
size must be a positive integer, validated by integer_validator
and the area() method must be implemented.
"""


Rectangle = __import__('9-rectangle').Rectangle

def integer_validator(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError('Size must be a positive integer')

class Square(Rectangle):
    """
    Use from 9-rectangle.py for the inherits of Square
    """
    def __init__(self, size):
        integer_validator(size)
        self._size = size
        super().__init__(width=size, height=size)

    def area(self):
        return self._size **  2
