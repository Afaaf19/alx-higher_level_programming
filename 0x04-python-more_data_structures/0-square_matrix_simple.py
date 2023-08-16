#!/usr/bin/python3
"""function that computes the square value of all integers of a matrix"""

def square_matrix_simple(matrix=[]):
    new_matrix = [[]] * len(matrix)

    for i, j in enumerate(matrix):
        new_matrix[i] = [x**2 for x in j]
    return new_matrix
