#!/usr/bin/python

def primeAnalysis(b):
    y = ''
    for x in range(0, b):
        if x > 1:
            if ( x % 2 != 0):
                y += str(x)

        x = int(x)
        x += 1


b= int(raw_input("How many numbers you wish to check: "))

response = primeAnalysis(b)

print response