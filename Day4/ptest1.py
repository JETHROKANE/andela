#!/usr/bin/python

def find_missing(a, b):
    z = []
    m = len(a)
    n = len(b)
    if m == n:
        k = 0
        return k
    else:
        for x in b:
            y = a.count(x)

            if y == 0:
                return x




