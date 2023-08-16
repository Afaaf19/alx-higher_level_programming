#!/usr/bin/python3
""" function that prints a dictionary by ordered keys"""

def print_sorted_dictionary(a_dictionary):
    for k in sorted(a_dictionary.keys()):
        print('{}: {}'.format(k, a_dictionary[k]))
