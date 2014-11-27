#!/usr/bin/env python

class Demo(object):
    def __init__(self, value):
	self.value = value

    def get_value(self):
	return self.value

    def __del__(self):  #destructor 
	print "%s : object is getting destoryed" % self

if __name__ == '__main__':
    d = Demo('a sample class')
    print d.get_value()
    print d.__class__.__name__   #get the name of the class the object which belong to
