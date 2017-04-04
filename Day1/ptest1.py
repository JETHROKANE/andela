#!/usr/bin/python
from __future__ import division

def primeAnalysis(b):
    y = ''

    if b > 1:
        for x in range(0, b):
            if ( b % x ) == 0:
                break
            else:
                y += str(x) + ','

        x = int(x)
        x += 1

    return y


b= int(input("How many numbers you wish to check: "))

response = primeAnalysis(b)

print (response)