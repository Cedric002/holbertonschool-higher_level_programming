#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    even the hidden ones.
    """

    return dir(obj)
