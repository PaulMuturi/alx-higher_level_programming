#!/usr/bin/python3
""""
This module provides a function to perform the add mathematical operation

Functions:
    add_integer: Adds two integers and returns the sum
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the sum

    Args:
        a (int or float): first number.
        b (int or float) : second number.

    Returns: Sum as as float or int

    Raises:
        TypeError: if either a or b or both are neither an int or float
    """
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
