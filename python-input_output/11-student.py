#!/usr/bin/python3
"""
Define a Student
"""


class Student:
    """
    class Student with a public instance attributes,
    first_name, last_name and age.
    a instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    A public method def to_json(self): that retrieves a dictionary
    representation of a Student instance.
    If attrs is a list of strings, only attribute names contained in this
    list must be retrieved.
    Otherwise, all attributes must be retrieved.
    A other Public method def reload_from_json(self, json): that replaces all
    attributes of the Student instance:
    json always is a dictionary,
    a dictionary key will be the public attribute name and
    a dictionary value will be the value of the public attribute
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return {'first_name': self.first_name, 'last_name': self.last_name,
                'age': self.age}

    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
