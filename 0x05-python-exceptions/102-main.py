#!/usr/bin/python3

magic_calculation = __import__('102-magic_calculation').magic_calculation

tests = [
    (2, 3),
    (1, 3),
    (5, 2),
    (10, 3),
    (0, 5),
    (-1, 2),
]

for a, b in tests:
    print("magic_calculation({}, {}) = {}".format(
        a, b, magic_calculation(a, b)
    ))
