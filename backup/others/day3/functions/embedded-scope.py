#!/usr/bin/env python

def summation(a, b):
    def add(x):
	return x + b  #b is avil from the embedded scope 
    return add(a)

print summation(11, 12)

print __name__

