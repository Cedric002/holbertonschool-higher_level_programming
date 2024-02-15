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
    And a public method def to_json(self): that retrieves a dictionary
    representation of a Student instance.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return
        {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
