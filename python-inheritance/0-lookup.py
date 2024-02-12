#!/usr/bin/python3
"""
This function returns the list of available attributes and
methods of an object.

obj (object): The object whose attributes and methods are to be listed.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    even the hidden ones.
    """

    return dir(obj)
