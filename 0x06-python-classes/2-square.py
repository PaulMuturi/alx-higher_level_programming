#!/usr/bin/python3
"""Square module
Classes:
    Square: defines a square and instantiates its size
"""


class Square:
    """This class defines square and instantiates it with private \
       instance attribute 'size'.
    """
    def __init__(self, size=0):
        """Instantiates instance attribute with value

            Args:
                size (int): size of square
            Raises:
                TypeError: if size is not an integer
                ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
