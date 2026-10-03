#!/usr/bin/python3
"""Module that defines the Base class."""


class Base:
    """Base class that manages the id attribute of all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): the id of the instance. If None, an id is
                assigned automatically by incrementing __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
