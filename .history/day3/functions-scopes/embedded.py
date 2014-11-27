#!/usr/bin/env python

def summation(a, b):
    def add(y):
        return a + y  # is available to the function add from the embedded scope, ie, none other than the scope where the function add is defined.
    return add(b)

print summation(20, 12)

