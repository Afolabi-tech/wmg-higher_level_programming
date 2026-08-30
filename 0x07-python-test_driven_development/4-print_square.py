#!/usr/bin/python3

"""
4-print_square.py

This module provides a single function, print_square which 
prints a square of size 'size' with the character '#'.
"""

def print_square(size):
    """ Prints a square of size 'size' with the character '#'
    Args:
        size must be an integer and not float or less than zero.

    Return:
        character #
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        print("#" * size)
    

