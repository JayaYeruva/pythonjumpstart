#!/usr/bin/python

def power(val):
   return  val[0] ** val[1]

def mymap(func, seq):
   return [ func(item) for item in seq]

print mymap(str.upper, ['a', 'b', 'c', 'd'])
print mymap(power, [(2,2), (2,3), (2,4)])
print map(power, [(2,2), (2,3), (2,4)])
