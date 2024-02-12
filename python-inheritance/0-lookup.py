#!/usr/bin/python3
def lookup(obj):
    """
    tThis function returns the list of available attributes and
    methods of an object.

    obj (object): The object whose attributes and methods are to be listed.

    Returns the list of available attributes and methods of an object
    even the hidden ones.
    """

    return dir(obj)
