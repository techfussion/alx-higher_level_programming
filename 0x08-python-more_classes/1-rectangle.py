#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """Class representation"""

    def __init__(self, width=0, height=0):
        """Global instantiation attributes.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
