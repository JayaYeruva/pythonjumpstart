#!/usr/bin/env python
'''
    a sample python modules 
'''

class Demo(object):
    '''
	a quick dummy class
    '''
    pass   

def headntail(filename, **param):
    '''
     headntail : a utility to do head and tail 
    '''
    lines = ''
    content = open(filename).readlines()
    count = param.get('count', 10)
    order = param.get('order', 'head')
    if order == 'head':
        lines = content[:count]
    elif order == 'tail':
        lines = content[-count:]
    return ''.join(lines)

def power(x, n):
    '''
     power return x to the power of n
    '''
    return x ** n

def swap(a, b):
    '''
	swap swap's two values
    '''
    return(b, a)

name = 'jaya'
version = '0.0.0b'
release = 'beffy cow'

