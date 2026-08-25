#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square.

        Args:
            size (int): The size of the new Square.
            position (tuple): The position of the new Square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets/sets the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets/sets the position of the Square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(type(num) is int for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the Square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the Square with the character '#'."""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)


    def __str__(self):
        """ Returns the string that my_print() would output. """
        if self.__size == 0:
            return()

        result = "\n" * self.__position[1]
        result += "\n".join(
                " " * self.__position[0] + "#" * self.__size
                for i in range(self.__size))

        return result

