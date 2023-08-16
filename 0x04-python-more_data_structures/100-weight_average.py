#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    nb1 = sum(x[0] * x[1] for x in my_list)
    nb2 = sum(x[1] for x in my_list)
    return nb1 / nb2
