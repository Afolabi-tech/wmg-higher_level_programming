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

    """
    def update(self, *args):
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
    """

    def update(self, *args, **kwargs):
        """Assigns attributes to the instance.

        *args order: id, width, height, x, y
        **kwargs is only used if *args is empty.
        """
        if args and len(args) != 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i >= len(attrs):
                    break
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if key in ("id", "width", "height", "x", "y"):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a rectangle """
        return {

                "id" : self.id,
                "width" : self.width,
                "height" :self.height,
                "x" : self.x,
                "y" : self.y
        }
