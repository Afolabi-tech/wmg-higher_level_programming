#!/usr/bin/python3


""" 
7-base_geometry.py

Defines BaseGeometry class
"""

class BaseGeometry:

    """ raises an Exception with the message area() is not implemented """
    def area(self):
        raise Exception("area() is not implemented")

    
    def integer_validator(self, name, value):
        
        """ Validates that value is a positive integer. """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
