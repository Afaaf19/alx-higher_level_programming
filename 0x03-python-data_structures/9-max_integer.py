#!/usr/bin/python3
"""function that finds the biggest integer of a list"""

def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    max = my_list[0]
    for nb in my_list:
        if max < nb:
            max = nb
    return max
