#!/usr/bin/python3

def islower(c):
    """check if a character is lower."""
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    return False
