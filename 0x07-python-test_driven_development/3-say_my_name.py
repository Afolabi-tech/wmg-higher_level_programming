#!/usr/bin/python3

"""
3-Say_my_name.py - <first name> <last name>

This module provides a function to print my name is <first name> <last name>
"""

def say_my_name(first_name, last_name = ""):
    
    """ Concatenate first_name and last_name,
        print out the fullname

    Args:
        first_name must be a string
        last_name must be a string
    Returns:
        My name
    
    """

    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")

    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
