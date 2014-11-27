#!/usr/bin/env python

class Box(object):
    def __init__(self, size):
	self.size = size
    
    def __add__(self, others):
	return Box( self.size + others.size)
    
    def __str__(self):   #overload str()
	return '<%s: size=%s>' % (self.__class__.__name__, self.size)
	

if __name__ == '__main__':
    b1 = Box(10)
    b2 = Box(20)
    b3 = b1 + b2  #try to overload + wrt box type  b1.__add__(b2)
    print b3
