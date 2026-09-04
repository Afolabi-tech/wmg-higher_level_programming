#!/usr/bin/python3
class LockedClass:
    """ A class that only allows a 'first_name' instance attribute. """

    __slots__ = ["first_name"]
