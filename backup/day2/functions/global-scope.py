#!/usr/bin/env python

n = 'pypi'   #lives in the global scope

def demo():
    global n
    n = 100   #lives in the local scope 
    print n
demo()
print n
