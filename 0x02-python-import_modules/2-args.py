#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    num_a = len(argv) - 1

    if num_a < 1:
        print("{} arguments.".format(num_a))
    elif num_a == 1:
        print("{} arguments:".format(num_a))
    else:
        print("{} arguments:".format(num_a))

    for d in range(num_a):
        print("{}: {}".format(d + 1, argv[d + 1]))
