#!/usr/bin/env python

class Box(object):
    def __init__(self, size):
	self.size = size 
  
    def __mul__(self, ntimes):
	return Box(self.size * ntimes)

    def __neg__(self):
	return Box(-self.size)

    def __add__(self, other):
	return Box(self.size + other.size)

    def __str__(self):
	return "<%s size=%s>" % (self.__class__.__name__, \
					self.size)

if __name__ == '__main__':
    b1 = Box(10)
    b2 = Box(11)
    b3 = b1 + b2   # b1.__add__(b2)
    print -(b3 * 3)


