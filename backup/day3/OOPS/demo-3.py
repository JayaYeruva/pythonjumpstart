#!/usr/bin/env python

class Demo(object):
    def __init__(self, value):
 	self.value = value

    def get_value(self):
	return self.value 

    def __del__(self):
	print "%s : destroying..." % self

if __name__ == '__main__':
    d = Demo('pypi')
    print d.get_value()
    
