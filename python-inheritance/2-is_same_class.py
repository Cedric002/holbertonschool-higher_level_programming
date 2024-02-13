#!/usr/bin/python3
"""
The function returns True if the object is exactly an instance of the specified class;
otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Returns True or False
    """

    return type(obj) is a_class
