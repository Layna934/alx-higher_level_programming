#!/usr/bin/python3

"""To calculate area of a square"""


class Square:
    """
    Square with area
    """

    def __init__(self, size=0):
        """
        raise exceptions first
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate the area"""
        area = self.__size * self.__size
        return area
