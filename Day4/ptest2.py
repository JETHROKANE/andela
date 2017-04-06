#!/usr/bin/python

class BinarySearch:
    """This is the binary search algorithm"""

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 0
        d = [self.b]
        self.e = self.a * self.b
        self.f = self.b

        while (self.f <= self.e):
            self.f += self.b
            d.append(self.f)
            self.c += 1

        self.d = d
        self.g = len(self.d)




    def search(self, g):
        if g == "count":
            return self.c
        elif g == "index":
            return self.f
        else:
            return [self.b, self.e, self.a]


#results = BinarySearch(20, 1)
#print results.search()
