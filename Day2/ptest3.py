#!/usr/bin/python

def fizz_buzz(a):
    if not isinstance(a, int):
        raise ValueError('Allow only numeric input')

    if a % 3 == 0 and a % 5 == 0:
        b = "FizzBuzz"

    elif a % 3 == 0:
        b = "Fizz"

    elif a % 5 == 0:
        b = "Buzz"

    else:
        b = a

    return b


