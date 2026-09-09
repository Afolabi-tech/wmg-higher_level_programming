#!/usr/bin/python3
""" The module that returns 'True' if the object is exactly an instance of the specific class.  """

def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True

    return False

    # Alternative method
    #return type(obj) is a_class
