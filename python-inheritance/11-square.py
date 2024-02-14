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

class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def print(self):
        return f"[Square] {self.__size}/{self.__size}"

    def str(self):
        return self.print()
