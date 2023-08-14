#!/usr/bin/python3
""" function that finds all multiples of 2 in a list"""

def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    newlist = []
    for nb in my_list:
        newlist.append(True if nb % 2 == 0 else False)
    return newlist
