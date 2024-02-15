#!/usr/bin/python3
"""
The function returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization
of an object.
"""


def class_to_json(obj):
    """
    Converts an object to a dictionary with simple data structures
    suitable for JSON serialization.
    """
    json_dict = {}

    for attr, value in obj.__dict__.items():
        json_dict[attr] = value

    return json_dict
