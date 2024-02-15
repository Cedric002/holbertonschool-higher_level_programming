#!/usr/bin/python3
"""
The function creates an Object from a “JSON file.
"""


import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


class ListManager:
    """
    Class responsible for managing a list and saving it to a JSON file.
    """

    def __init__(self, filename='add_item.json'):
        self.filename = filename
        self.my_list = []

    def append_items(self, items):
        self.my_list += items

    def save_to_file(self):
        save_to_json_file(self.my_list, self.filename)

    def load_from_file(self):
        return load_from_json_file(self.filename)


def main():
    args = sys.argv[1:]
    list_manager = ListManager()
    list_manager.append_items(args)
    list_manager.save_to_file()


if __name__ == "__main__":
    main()
