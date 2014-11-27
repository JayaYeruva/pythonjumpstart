#!/usr/bin/env python

def mymap(f_name, seq):
     return [ f_name(item) for item in seq ]

l = range(1,11)
print mymap(str, l)
