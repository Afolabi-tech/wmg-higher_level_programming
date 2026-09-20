#!/usr/bin/python3
"""Module that defines a function to insert text after matching lines."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a specific string.

    Args:
        filename: the name of the file to modify.
        search_string: the string to look for in each line.
        new_string: the text to insert after each matching line.
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
