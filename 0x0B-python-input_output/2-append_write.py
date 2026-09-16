#!/usr/bin/python3

def append_write(filename="", text=""):
    """Appends text to a UTF8 file and returns the number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
