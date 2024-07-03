#!/usr/bin/python3

"""
Defines class that inherits from the list class
"""


class MyList(list):
    """
    Inherits from list class
    """
    def print_sorted(self):
        """
        prints sorted list
        """

        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
