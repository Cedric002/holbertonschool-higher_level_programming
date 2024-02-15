#!/usr/bin/python3
"""
The function reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its contents to stdout.
    """

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end='')
