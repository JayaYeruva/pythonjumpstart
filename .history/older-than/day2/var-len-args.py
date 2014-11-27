#!/usr/bin/env python

def sum(*args):
  tot = 0
  for item in args:
      tot += item
  return tot

print sum()
print sum(5)
print sum(1,2,3,4,5)
l = range(10)
print sum(*l)
t = tuple(l)
print sum(*t)

