#!/usr/bin/env python

class Box(object):
    def __init__(self, size):
	self.size = size 

    def boxdecor(func):
	def getit(self):
	    return "[ %s ]" % func(self)
	return getit

    @boxdecor
    def get_size(self):
	return self.size

if __name__ == '__main__':
    b = Box(10)
    print b.get_size()  # call the inner function 
