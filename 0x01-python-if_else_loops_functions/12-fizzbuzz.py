#!/usr/bin/python3


def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            value = "FizzBuzz"

        elif i % 5 == 0:
            value = "Buzz"

        elif i % 3 == 0:
            value = "Fizz"

        else:
            value = i

        if i == 100:
            print (value)

        else:
            print(value, end = ", ")

       
