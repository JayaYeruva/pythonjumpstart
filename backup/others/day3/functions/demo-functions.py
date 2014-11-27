#!/usr/bin/env python

def compute(n):
    return n**2, n**3

print compute(5); exit(1)

def demo():
   print 'a sample python function'

demo()

def power(x=0, n=0):  #default arg functions
    return x ** n

print power(2, 3)
print power(2)
print power()
