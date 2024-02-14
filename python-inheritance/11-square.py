#!/usr/bin/python3
"""
The function print class Square that inherits from Rectangle with
instantiation with size: def __init__(self, size): .
size must be private. No getter or setter,
size must be a positive integer, validated by integer_validator
and the area() method must be implemented.
print() should print, and str() return [Square] <width>/<height>
"""


Rectangle = __import__('9-rectangle').Rectangle

class Rectangle:

class Square(Rectangle):
    def __init__(self, size):
        if not integer_validator(size):
            raise ValueError("Size must be a positive integer")
        self._size = size
        super().__init__(size, size)

    def area(self):
        return self._size **  2

    def __str__(self):
        return "[Square] {}/{}".format(self._size, self._size)

    def print(self):
        print(self.__str__())
