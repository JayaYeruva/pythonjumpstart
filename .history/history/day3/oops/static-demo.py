#!/usr/bin/env python

class People(object):
    counter = 0   #static variable

    def __init__(self, pid):
	self.pid = pid
	People.counter += 1

    def check_limit():
	return True if People.counter < 10 else False 

    check_limit = staticmethod(check_limit) #static method

    def __str__(self):
	return "%s pid=%s" % (self.__class__.__name__, self.pid)

if __name__ == '__main__':
    p = []
    for i in range(1, 14):
        if People.check_limit():
               p.append(People(i))
        else:
	    print "%s: max populaton limit reached" % \
				p.__class__.__name__
            break
	
    for item in p:
	print item

