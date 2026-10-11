#!/usr/bin/python3
"""Module that defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square is a Rectangle with the same width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square.

        Args:
            size (int): width and height of the square.
            x (int): horizontal offset.
            y (int): vertical offset.
            id (int): identifier of the instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
