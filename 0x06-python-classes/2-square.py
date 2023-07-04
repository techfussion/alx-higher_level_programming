#!/usr/bin/python3
"""Define a square object"""


class Square:
    """Object representation"""

    def __init__(self, size=0):
        """ Initialize new public attributes

        Args:
            size(int) : Represents the size of the square
        """

        if isinstance(size, (int)):
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
