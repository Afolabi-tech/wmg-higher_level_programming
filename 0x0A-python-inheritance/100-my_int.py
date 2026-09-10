#!/usr/bin/python3

""" defines the MyInt class """

class MyInt(int):
    """ A rebel integer with inverted == and != operators. """

    def __eq__(self, other):
        """ Invert the == operator."""
        return int(self) != other

    def __ne__(self, other):
        """ Invert the != operator. """
        return int(self) == other
