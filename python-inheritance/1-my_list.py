#!/usr/bin/python3
"""
Define a class MyList.
"""


class MyList(list):
    """
    The class MyList lets you write inherits from list.
    The public instance method prints the list in ascending sort.
    """

    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
