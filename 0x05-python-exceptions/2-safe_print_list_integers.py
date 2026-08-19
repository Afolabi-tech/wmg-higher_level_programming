#!/usr/bin/python3

def safe_print_list_integers(my_list = [], x = 0):

    index = 0
    printed = 0

    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            printed += 1

        except (ValueError, TypeError, IndexError):
            if index >= x:
                break

        index += 1

    print()
    return printed

