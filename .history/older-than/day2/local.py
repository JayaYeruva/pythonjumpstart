#!/usr/bin/env python

n = 100 #global


def test():
  global n
  n = 102
  print id(n)
  n = 103
  print id(n)
  print n 

test()
print id(n) 
print n
