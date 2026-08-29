#!/usr/bin/python3
"""
2-matrix_divided.py

this module privides a single function, matrix_divided, 
which divides all elements of matrix by a given divisor.
"""

def matrix_divided(matrix, div):
    """
    Divide  all the elements of a matrix by div, rounded to 2 decimals.
    """

    if (not isinstance(matrix, list) or len(matrix) == 0 or not all(
            isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) == 0 or not all(
                isinstance(item, (int, float)) for item in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError(
            "Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]

    return new_matrix
