#!/usr/bin/python3

"""
This a print_square module

Functions:
    print_square: prints a square of a given length\
    using a # character
"""


def print_square(size):
    """
    Prints a square of a given length with the character #

    Args:
        size: length of the square
    Returns: Nothing
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        TypeError: if size is a float and is less than 0
    """

    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size >= 0:
       raise TypeError("size must be an integer")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
