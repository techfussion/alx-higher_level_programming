#!/usr/bin/python3
"""Integer summation"""


def add_integer(a, b=98):
    """Adds a to b and return the result.

    Atrributes:
        a (float, int): The first number to sum.
        b (flaot, int): The second number to sum.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)

    return a+b
