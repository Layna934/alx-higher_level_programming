#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lilen = len(my_list)
    if idx < 0 or idx >= lilen:
        return (my_list)
    else:
        new_li = my_list.copy()
        new_li[idx] = element
        return (new_li)
