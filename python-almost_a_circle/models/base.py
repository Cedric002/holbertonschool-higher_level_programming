#!/usr/bin/python3
"""
Define a class Base.
The private instance initialized to 0.
In a class constructor: def __init__(self, id=None): :
if id is not None, public instance attribute id with this argument value,
otherwise increment __nb_objects and assign the new value to the
public instance attribute id.
Update: adding the static method def to_json_string(list_dictionaries):
that returns the JSON string representation of list_dictionaries.
Update: adding the class method def save_to_file(cls, list_objs):
that writes the JSON string representation of list_objs to a file.
"""

import json



class Base:
    """
    The class Base for the "base" of all other classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    """
    Static method that returns the JSON string representation
    of list_dictionaries
    """
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    """
    Class method that writes the JSON string representation
    of list_objs to a file
    """
    def save_to_file(cls, list_objs):
        class BaseEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, Base):
                    return obj.to_dictionary()
                return super().default(obj)

        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            json_str = json.dumps(list_objs, cls=BaseEncoder)
            f.write(json_str)
