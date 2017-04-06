#!/usr/bin/python
import re


def words(a):
    a = str(a)
    b = a.split()
    c = {}
    for x in b:
        try:
            y=a.count(x)
            x = int(x)
            c[x] = y
        except:
            a = a.replace('\t', a)
            y = len(re.findall(x, a))
            c[x] = y

    return c

a = "car : carpet as java : javascript!!&@$%^&"
response = words(a)

print str(response)