#!/usr/bin/python3
"""
The function returns True if the object is an instance of a class that
inherited from or the specified class;
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True or False
    """

    return isinstance(obj, a_class)
