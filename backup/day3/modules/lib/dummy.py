#!/usr/bin/env python
'''
dummy
a dummy python module
author : jaya
'''

name='dummy'
author='jaya'
version='0.0.1 beta'

def get_output(cmd):
    '''
    get_output(cmd) String
    gets you the output of the given command
    '''
    from subprocess import check_output
    return check_output(cmd, shell=True)

def swap(a, b):
    '''
    swap(a, b) Tuple
    swap swap's the arguments, returns (b, a)
    '''
    return b, a

class Demo(object):
    '''
    Demo
    a dummy Type Demo
    '''
    pass

if __name__ == '__main__':
    print __name__
    print name
    print get_output('ls -l')
    print swap(10, 'pete') 

