#!/usr/bin/env python

n = 100  #global scope 

def demo():
   global n  # to refer global version of n instead of creating a local variable
   n = 'python'   #local scope, local to the function demo
   print n

demo()
print n
