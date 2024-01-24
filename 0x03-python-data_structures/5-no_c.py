#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for letter in my_string:
        if letter.lower() != 'c':
            string += letter
    else:
        return string
