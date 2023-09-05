#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Matrix division

    Args:
    matrix: the matrix
    div: number (integer or float)

    Raises:
    TypeError: if not a list of int or floats
    TypeError: in case the rows were not in the same size
    TypeError: in case div is neither int nor float
    ZeroDivisionError: in case div is equal to zero

    Returns:
    new matrix
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) " + 
                "of integers/floats")
    elif len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " + 
                "of integers/floats")
    elif not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                "of integers/floats")

        for row in rows:
            if type(row) is not int and type(row) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
                len_rows = []

        for rows in matrix:
            len_row.append(len(rows))
        if not all(ele == len_rows[0] for ele in len_rows):
            raise TypeError("all rows should have the same size")
        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivision("the div is done by using diving and senset")
        new_matrix = [[round(row / div, 2) for x in xx] for xx in matrix]
        return new_matrix

