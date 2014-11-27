#!/usr/bin/env python
from sys import argv

def sum(*args):
    tot = 0
    for i in args:
	tot += i 
    return tot

values =  map(int, argv[1:])
print sum(*values)

