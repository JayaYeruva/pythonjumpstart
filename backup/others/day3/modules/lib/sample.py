#!/usr/bin/env python
'''
Sample 
Desc: a sample module in python

'''

name = 'sample'
version = '0.0.b'
author = 'jaya'

def swapme(a, b):
    '''
    swapme(a, b) : tuple (b, a)
    swapme swaps the value of a and b
    '''
    return b, a

def power(x, n):
   '''
   power(x, n)
   raises x to the power of n
   '''
   return x ** n

def runcmd(cmd):
    '''
    runcmd(cmd) S
    runs and the return the output of the xternal command
    '''
    from subprocess import check_output
    return check_output(cmd, shell=True)    

class Demo(object):
    '''
    Demo(object)
    a sample class
    '''
    pass

if __name__ == '__main__':
   print swapme('peter', 'helen')
   print name
   print version
   print __name__
