#!/usr/bin/python
#from __future__ import division

def primeAnalysis(b):

    if not isinstance(b, int):
        raise ValueError('The provided input is not an intiger.')

    y = ''

    for x in range(0, b + 1):
        if x > 1:
            for n in range(2, x):
                if (x % n) == 0:
                    break
            else:
                y += str(x) + ','


    return y


b = int(input("How many numbers you wish to check: "))

response = primeAnalysis(b)

print (response)