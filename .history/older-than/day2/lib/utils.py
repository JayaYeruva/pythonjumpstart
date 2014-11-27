#!/usr/bin/env python
'''
    Utils Module
    a sample python module for the utils

    Name : jaya
    Date :  Aug 30 2013
'''
class Utils(object):
    '''
	a utils class
        a demo class for writing the modules
    '''
    def __init__(self):
        pass

    def getCWD(self):
        '''
            getCWD()   return cwd
	    method for the Ultils class
        '''
	pass

def power(x, n):
   '''
	a function to raise x to the power of n
   '''
   return x ** n

version = '0.0.1b'
author = 'jaya'
lang = 'python'

if __name__ == '__main__':
    print power(2,3)


 
