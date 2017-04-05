#!/usr/bin/python

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
            y = a.count(x)
            c[x] = y

    return c

a = "testing 1 2 testing"
response = words(a)

print str(response)