#!/usr/bin/python3

'''A function that adds integers and floats'''


def add_integer(a, b=98):
    '''Returns addition of arguments
    Raises:
        TypeError if either argument is neither an int or a float
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    result = int(a) + int(b)

    return result
