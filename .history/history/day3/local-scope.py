#!/usr/bin/env python

n = 100   #global scope 


def demo22():
   n = 100      #local variable
   print n

def demo():
   global n       #help to refer the n from the global scope
   n = 'python'   
   print n


demo()
print n

print __name__   #builtins
