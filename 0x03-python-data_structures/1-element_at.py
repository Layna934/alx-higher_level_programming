#!/usr/bin/python3
def element_at(my_list, idx):
    lilen = len(my_list)
    if idx < 0:
       return None
    if idx >= lilen:
       return None
    else:
        return my_list[idx]
