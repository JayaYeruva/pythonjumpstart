#!/usr/bin/env python

class Box(object):
    def __init__(self, side):
	self.side = side

    def __add__(self, others):
	return Box(self.side + others.side)

    def __mul__(self, times):
	return Box(self.side * times)
 
    def __str__(self):
	return "<%s side=%s>" % (self.__class__.__name__, self.side)
   
b1 = Box(10)
b2 = Box(12)
b3 = b1 + b2    # + overloaded 
b4 = b1 * 4;
print b3
print b4
