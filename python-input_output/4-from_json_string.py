#!/usr/bin/python3
"""
The function returns an object (Python data structure)
represented by a JSON in string type.
"""


import json


def from_json_string(my_str):
    """
    Converts a JSON string into a Python object.
    """
    return json.loads(my_str)
