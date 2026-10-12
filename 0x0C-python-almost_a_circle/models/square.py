#!/usr/bin/python3
"""Module that defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square is a Rectangle with the same width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes to the instance.

        *args order: id, size, x, y
        **kwargs is only used if *args is empty.
        """
        if args and len(args) != 0:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i >= len(attrs):
                    break
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if key in ("id", "size", "x", "y"):
                    setattr(self, key, value)

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
