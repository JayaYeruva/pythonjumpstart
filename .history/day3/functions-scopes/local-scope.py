#!/usr/bin/env python

n = 100  #local variable to the script

def demo():
    n = 'perl'    #local is local to the function 
    print n

if 1 == 1:
   name = 'larry'  # its possible, its too take it into the scope of the script

print name
demo()
print n
