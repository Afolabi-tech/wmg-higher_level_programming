#!/usr/bin/python3
"""Writes a UTF8 string to a file and returns the number of characters. """

def write_file(filename="", text=""):
    with open(filename,"w", encoding = "utf-8") as f:
        return (f.write(text))
