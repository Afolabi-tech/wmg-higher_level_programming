#!/usr/bin/python3

def uppercase(str):
    """Prints a string in uppercase followed by a new line"""
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print("{:c}".format(ord(c) - 32), end = "")
        
        else:
            print("{:c}".format(ord(c)), end = "")

    print()
        
