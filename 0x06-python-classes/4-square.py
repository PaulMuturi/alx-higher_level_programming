#!/usr/bin/python3
"""Square module
Classes:
    Square: defines a square
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
        self.size = size

    @property
    def size(self):
        """Getter for attribute size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for attribute size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of square of given size"""
        return self.__size ** 2
