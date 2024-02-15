#!/usr/bin/python3
"""
The function writes an Object to a text file, using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
