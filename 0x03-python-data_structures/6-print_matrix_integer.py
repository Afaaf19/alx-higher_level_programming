#!/usr/bin/python3
"""function that prints a matrix of integers"""

def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for elem in r:
            print('{:d}'.format(elem), end=' '
                    if elem != r[-1] else "")
        print()
