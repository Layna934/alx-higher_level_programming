#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length <= 0:
        return None
    else:
        max_val = my_list[0]
        for i in range(0, length):
            if my_list[i] > max_val:
                max_val = my_list[i]
        return max_val
