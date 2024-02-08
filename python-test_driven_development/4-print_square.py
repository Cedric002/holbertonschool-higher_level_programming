#!/usr/bin/python3
def print_square(size):
    """
    Print a square with the character #.
    size is the size length pf the square.

    size must be an integer.
    Otherwise: TypeError (size must be an integer).

    if size < 0.
    Otherwise: ValueError (size must be >= 0).

    if size is a float and < 0.
    Otherwise: TypeError (size must be an integer)

    Returns a square with #
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=  0")
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size <  0:
        raise ValueError('size must be >=  0')

    for nb in range(size):
        print('#' * size)
