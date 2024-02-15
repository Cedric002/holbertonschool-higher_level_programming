#!/usr/bin/python3
"""
The function writes a string to a text file and returns the number of
characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a UTF-8 encoding and returns the number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        num_chars_written = f.write(text)
    return num_chars_written
