#!/usr/bin/env python

class Demo(object):
    def __init__(self):
        print "contructor...."
	print self

    def __del__(self):
	print "%s : destroying..." % self

if __name__ == '__main__':
    d = Demo()
    print d
    
