#!/usr/bin/python3
""" function that prints all integers of a list, in reverse order"""

def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for x in range(len(my_list)):
            print("{:d}".format(my_list[::-1][x]))
