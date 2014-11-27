#!/usr/bin/env python
'''
    Utils22
    a sample python module
    Author : jaya
'''

def swap(a, b):
    '''
	swap(a, b) : return tuple
        swap() swaps the arguments
    '''
    return b ,a 


def power(x, n):
    '''
	power(x, n): return int
        power() raises x to the power of n
    '''
    return x ** n

class Demo(object):
    '''
	Demo(object)
	a sample python class
    '''
    
    def pprint(self):
	'''
	    pprint():
	    a sample method
        '''
        pass 

author = 'jaya'
version = '0.0.2'
pi = 3.142
if __name__ == '__main__':
   print version
   print pi
   print swap(10, 20)
   print power(2,3)



