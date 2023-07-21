#!/usr/bin/python3
"""Contains function that divides all element of a matrix"""


def matrix_divided(matrix, div):
    """Validates and divide matrix(matrix) by its divident(div).

    Attributes:
        matrix (list of lists): list of lists containing int/float dt.
        div (int, flaot): value to divide the matrix by (diivdent)..
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """

    for item in matrix:
        if not isinstance(item, list) or
                any(not isinstance(i, (int, float)) for i in item):
            raise TypeError("matrix must be a matrix (list of lists) of"
                "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for item in matrix:
        new_matrix.append([round(res/div, 2) for res in item])

    return new_matrix
