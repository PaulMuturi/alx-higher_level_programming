#!/usr/bin/python3
"""Square module
Classes:
    Square: defines a square and instantiates its size
"""


class Square:
    """This class defines square and instantiates it with private \
       instance attribute 'size'

       Attributes:
            size: size of square
    """
    def __init__(self, size):
        """Instantiates instance size attribute"""
        self._size = size
