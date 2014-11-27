#!/usr/bin/env python

def mymap(func, seq):
    return [ func(i) for i in seq ]


l = ['amanda', 'aman', 'amit']

print map(str.title, l)
print map(str.upper, l)

print mymap(str.title, l)
print mymap(str.upper, l)
