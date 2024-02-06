#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two numbers who should are integers.

    a: number 1, if is a float, converted to an integer.
    b: number 2. Defaults to  98. If is a float, converted to an integer.

    TypeError: If a or b is not an integer or float.

    Returns the sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
