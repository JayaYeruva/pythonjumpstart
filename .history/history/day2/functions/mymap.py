#!/usr/bin/env python

def mymap(func, seq):
    return [func(i) for i in seq]


l = [2,1,3,4,5]

print map(bin, l)
print mymap(bin, l)
