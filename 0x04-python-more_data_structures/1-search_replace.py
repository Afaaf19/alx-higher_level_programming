#!/usr/bin/python3
""" function that replaces all occurrences of an element by another in a new list"""

def search_replace(my_list, search, replace):
    return [nb if not nb == search else replace for nb in my_list]
