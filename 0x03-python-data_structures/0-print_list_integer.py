#!/usr/bin/python3
def print_list_integer(my_list=[]):
    listlen = len(my_list)
    a = 0
    while a < listlen:
        print("{}".format(my_list[a]))
        a += 1
