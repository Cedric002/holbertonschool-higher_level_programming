#!/usr/bin/python3
"""
Define a class Base.
The private instance initialized to 0.
In a class constructor: def __init__(self, id=None): :
if id is not None, public instance attribute id with this argument value,
otherwise increment __nb_objects and assign the new value to the
public instance attribute id.
"""


class Base:
    """
    The class Base for the "base" of all other classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
