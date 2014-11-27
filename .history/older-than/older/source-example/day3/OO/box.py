#!/usr/bin/python

class Box(object):
    def __init__(self, size):
	self.size = size
    
    def __str__(self):
        return "< Box : size = %s>" % self.size	

    # overload +
    def __add__(self, obj):
	return Box(self.size + obj.size)


b1 = Box(5)
b2 = Box(15)
b3 = b1 + b2
#b3 = b1.__add__(b2) 
print b3
	
