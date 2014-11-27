#!/usr/bin/env python

def add(seq):
    tot = 0
    for item in seq:
	tot +=  item
    return tot

print add([])
print add([2,4,6])
print add((2,4,6))
