#!/usr/bin/python3
"""
The function print class BaseGeometry with
public instance method: def area(self): .
Oterwise message (Exception area() is not implemented).
A public instance method: def integer_validator(self, name, value): that value:
name is string,
if value is not an integer: Oterwise TypeError (<name> must be an integer),
if value <= 0: oterwise ValueError (<name> must be greater than 0).
"""


class BaseGeometry:
    """
    The classe define a geometrie.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
