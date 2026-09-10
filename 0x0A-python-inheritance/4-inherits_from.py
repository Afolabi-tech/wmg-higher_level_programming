#!/usr/bin/python3

""" 
inherits_from.py

This module provides a single function, inherits_from, which checks whether an object is an instance of a class that inherited
(directly or indirectly) from a specific class.
"""

def inherits_from(obj, a_class):

    return isinstance(obj, a_class) and type(obj) is not a_class
