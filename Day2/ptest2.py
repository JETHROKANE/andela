#!/usr/bin/python
# -*- coding: utf-8 -*-

def data_type(a):
    if isinstance(a, str):
        return len(a)
    elif isinstance(a, bool):
        return a
    elif isinstance(a, list):
        try:
            return a[2]
        except:
            return None
    elif isinstance(a, type(None)):
        b = "no value"
        return b
    elif isinstance(a, int):
        if a > 100:
            b = "more than 100"
        elif a < 100:
            b = "less than 100"
        elif a == 100:
            b = "equal to 100"
        return b
