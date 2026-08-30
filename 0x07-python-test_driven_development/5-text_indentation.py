#!/usr/bin/python3

""" 5-text_indentation.py

This module provides a single function, text_indentation, which
prints a text with 2 new lines after each '.', '?', and ':'.

"""

def text_indentation(text):
    """ prints a text with 2 new lines after
    each of these characters: '.', '?' and ':'
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    stripped = text.strip()
    line = ""


    for char in stripped:
        if char == " " and (line == "" or line[-1] == " "):
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""

        elif char == "\n":
            print(line.strip())
            line = ""

    
    if line.strip():

        print(line.strip())
