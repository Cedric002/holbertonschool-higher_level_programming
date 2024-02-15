#!/usr/bin/python3
"""
The function returns the JSON representation of an object in string type.
"""


import json

def to_json_string(my_obj):
    """
    Converts a Python object to a JSON in string type
    """
    return json.dumps(my_obj)
