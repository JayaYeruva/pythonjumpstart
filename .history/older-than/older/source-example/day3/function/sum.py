#!/usr/bin/env python

def sum(seq):
    tot = 0
    for item in seq:
        tot += item
    return tot
data = input('Enter the value : ')
if type(data) == type(()) or type(data) == type([]):
    print sum(data)
else:
    print "invalid IP"; exit(1)
