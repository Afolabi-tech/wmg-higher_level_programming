#!/usr/bin/python3
"""Module that defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle (setters validate every value)."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__validate_non_negative("y", value)
        self.__y = value

    @staticmethod
    def __validate_integer(name, value):
        """Raise TypeError if value is not an integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    @staticmethod
    def __validate_positive(name, value):
        """Validate width/height: integer and > 0."""
        Rectangle.__validate_integer(name, value)
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def __validate_non_negative(name, value):
        """Validate x/y: integer and >= 0."""
        Rectangle.__validate_integer(name, value)
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        return self.__width * self.__height

    def display(self):
        if self.__width == 0 or self.__height == 0:
            return
        print("\n" * self.y, end = "")
        for _ in range(self.__height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        return "[rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
