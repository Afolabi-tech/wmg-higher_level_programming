#!/usr/bin/python3
"""
100-matrix_mul.py

This module provides a single function, lazy_matrix_mul, which
multiplies two matrices using the numpy module.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices m_a and m_b using numpy.

    """
    return np.matmul(m_a, m_b)
