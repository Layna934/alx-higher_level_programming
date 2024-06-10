#!/usr/bin/python3

"""Define Square where size is the size of square"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0):
        """Instance of square
        With size size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
