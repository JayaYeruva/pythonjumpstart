#!/usr/bin/env python

def sum(seq):
    tot =0
    for item in seq:
	tot += item
    return tot

print sum(())
print sum([1,2,3])
print sum((5,6,7,8))
