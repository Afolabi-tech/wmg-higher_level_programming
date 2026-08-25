#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (float/int): The size of the new Square.
        """
        self.size = size

    @property
    def size(self):
        """Gets/sets the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the Square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Checks if two Squares have equal area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two Squares have different areas."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Checks if this Square's area is greater than other's."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if this Square's area is greater than or equal to other's."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Checks if this Square's area is less than other's."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if this Square's area is less than or equal to other's."""
        return self.area() <= other.area()
