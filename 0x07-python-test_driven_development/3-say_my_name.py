#!/usr/bin/python3

"""
This is a say_my_name module

Functions:
    say_my_name: Prints a formatted string\
    containing first and last name of a person
Args:
    first_name: first name string
    last_name: last name string
Returns:
    Nothing
Raises:
    TypeError: if any of the names is not a string
"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
