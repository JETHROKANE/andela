#!/usr/bin/python

def find_max_min(a):
    b = max(a)
    c = min(a)

    if b == c:
        d = [len(a)]
    else:
        d = [c, b]

    return d

a = [4, 4, 4, 4, 4]
response = find_max_min(a)

print response