#!/usr/bin/env python
y = 100
def sum(x):
    global y
    def add(value):
       return value + y
    return add(x)

print sum(10) 
