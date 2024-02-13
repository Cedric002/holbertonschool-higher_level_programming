#!/usr/bin/python3
"""
The function print class BaseGeometry with
public instance method: def area(self): .
Oterwise (message area() is not implemented).
"""


class BaseGeometry:
    """
    The classe define a geometrie.
    """
    def area(self):
        raise NotImplementedError('area() is not implemented')
