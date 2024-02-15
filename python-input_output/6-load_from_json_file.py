#!/usr/bin/python3
"""
The function creates an Object from a “JSON file.
"""


import json


def load_from_json_file(filename):
    """
    Loads a JSON file and returns the contents as a Python object.
    """
    with open(filename, 'r') as file:
        return json.load(file)
