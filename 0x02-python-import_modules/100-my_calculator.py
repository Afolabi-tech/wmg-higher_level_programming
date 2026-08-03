#!/usr/bin/python3

"""
Import functions from calculator_1.py and performs
basic arithmetic operations.
"""
from calculator_1 import add, sub, mul, div
import sys


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./100-calculator.py <a> operator <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    operators = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div,
    }

    if op not in operators:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    result = operators[op](a,b)
    print("{} {} {} = {}".format(a, op, b, result))
