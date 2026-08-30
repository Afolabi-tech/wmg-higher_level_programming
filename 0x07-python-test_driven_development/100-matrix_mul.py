#!/usr/bin/python3
"""
101-matrix_mul.py

This module provides a single function, matrix_mul, which
multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices m_a and m_b.

    """
    for name, matrix in (("m_a", m_a), ("m_b", m_b)):
        if not isinstance(matrix, list):
            raise TypeError("{} must be a list".format(name))

    for name, matrix in (("m_a", m_a), ("m_b", m_b)):
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("{} must be a list of lists".format(name))

    for name, matrix in (("m_a", m_a), ("m_b", m_b)):
        if matrix == [] or matrix == [[]]:
            raise ValueError("{} can't be empty".format(name))

    for name, matrix in (("m_a", m_a), ("m_b", m_b)):
        for row in matrix:
            if not all(
                    isinstance(item, (int, float)) and
                    not isinstance(item, bool)
                    for item in row):
                raise TypeError(
                    "{} should contain only integers or floats".format(
                        name))

    for name, matrix in (("m_a", m_a), ("m_b", m_b)):
        row_size = len(matrix[0])
        if not all(len(row) == row_size for row in matrix):
            raise TypeError(
                "each row of {} must be of the same size".format(name))

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            new_row.append(total)
        result.append(new_row)

    return result
