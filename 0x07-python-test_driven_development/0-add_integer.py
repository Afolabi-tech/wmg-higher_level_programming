#!/usr/bin/python3

"""
0-add_integer.py

This module provides a single function, add_integer, which adds
two numbers (integers or floats) together and returns the sum
as an integer.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats and return the result as an integer.

    Args:
        a: first number, must be an int or float.
        b: second number, must be an int or float (default is 98).

    Returns:
        int: the sum of a and b, cast to an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
