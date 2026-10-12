#!/usr/bin/python3
"""Module that defines the Base class."""

import json
import csv
import turtle

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of the list_dictionaries. """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:              
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from <Class name>.json."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes list_objs to <Class name>.csv."""
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(filename, "w", newline="") as f:
            if list_objs is None:
                return
            writer = csv.writer(f)
            for obj in list_objs:
                writer.writerow([getattr(obj, field) for field in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances loaded from <Class name>.csv."""
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        try:
            with open(filename, "r", newline="") as f:
                reader = csv.reader(f)
                instances = []
                for row in reader:
                    if not row:
                        continue
                    dictionary = {}
                    for field, value in zip(fields, row):
                        dictionary[field] = int(value)
                    instances.append(cls.create(**dictionary))
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all Rectangles and Squares."""
        screen = turtle.Screen()
        screen.title("Almost a circle")
        screen.bgcolor("white")

        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.pensize(3)

        colors = ["red", "blue", "green", "orange", "purple", "brown"]

        def draw_shape(obj, width, height, color):
            t.penup()
            t.goto(obj.x, obj.y)
            t.setheading(0)
            t.color("black", color)
            t.pendown()
            t.begin_fill()
            for _ in range(2):
                t.forward(width)
                t.right(90)
                t.forward(height)
                t.right(90)
            t.end_fill()
            t.penup()

        for i, rect in enumerate(list_rectangles or []):
            draw_shape(rect, rect.width, rect.height, colors[i % len(colors)])

        for i, sq in enumerate(list_squares or []):
            draw_shape(sq, sq.size, sq.size, colors[(i + 3) % len(colors)])

        screen.exitonclick()
