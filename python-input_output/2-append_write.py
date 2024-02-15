#!/usr/bin/python3
"""
The function writes a string at the end of a text file and
returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a given text string to the end of a file specified by filename.
    Returns the number of characters added.
    """
    text = text.encode('utf-8')

    with open(filename, 'ab') as file:
        file.write(text)

    return len(text)
