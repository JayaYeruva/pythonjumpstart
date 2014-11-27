#!/usr/bin/env python
names = ['alphine', 'patric', 'nelson', 'jacobson']

def mymap(func, seq):
    return [ func(item) for item in seq ]

print map(str.upper, names)
print mymap(str.upper, names)
