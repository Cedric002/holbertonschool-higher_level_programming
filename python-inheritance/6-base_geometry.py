#!/usr/bin/python3
"""
The function print class BaseGeometry with
public instance method: def area(self): .
Oterwise message (Exception area() is not implemented).
"""


class BaseGeometry:
    """
    The classe define a geometrie.
    """
    def area(self):
        raise Exception('area() is not implemented')
