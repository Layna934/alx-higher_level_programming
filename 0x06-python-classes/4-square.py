#!/usr/bin/python3
"""
creating square class
"""
class Square:
    """
    setting attributes and methods for class
    """
    def __init__(self, size=0):
        """
        Initializing the square
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size

    @property
    """size getter"""
    def size(self):
        return(self.__size)

    @size.setter
    """size setter"""
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculating area of square"""
        area = self.__size * self.__size
        return area
