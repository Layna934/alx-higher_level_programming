#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = -1
    lilen = len(my_list)
    while idx >= -lilen:
        print("{}".format(my_list[idx]))
        idx -= 1
