#!/usr/bin/env python

class Demo(object):
    def __init__(self):
        print '%s: constructor' % self
  
    def getValue(self):
	print self

    def __del__(self):
        print '%s : destructor' % self


d = Demo()
print '%s : information of the object' % d
d.getValue()
