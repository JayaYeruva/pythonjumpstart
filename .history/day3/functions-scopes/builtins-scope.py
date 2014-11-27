#!/usr/bin/env python
'''
    a quick demos for the builtins scope
'''
#n = 100  #local variable to the script

def demo():
    global n
    n = 'python'
    print n

#demo()
#print n

print __name__
print __doc__
