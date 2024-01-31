#!/usr/bin/python3

"""
text_indentation module

Functions:
    text_indentation: indents and prints a a given string\
    based on delimeters specified
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text: string to indent
    Returns: nothing
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_str = ""
    for ch in text:
        current_str += ch

        if ch == '.' or ch == '?' or ch == ':':
            current_str = current_str.strip()
            print(f"{current_str}\n")
            current_str = ""

    current_str = current_str.strip()
    print(f"{current_str}", end='')
