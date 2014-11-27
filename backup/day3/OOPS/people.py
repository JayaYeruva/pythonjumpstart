#!/usr/bin/env python

class People(object):
    MAX = 5
    counter = 0

    def __init__(self, pid):
	People.check4limit()
	self.pid = pid
	People.counter += 1

    @staticmethod
    def check4limit():
	if People.counter > People.MAX:
	     raise Exception, 'max limit reached' 

#    check4limit = staticmethod(check4limit)
	
if __name__ == '__main__':
     p = []
     for pid in range(1, 9):
	p.append( People(pid) )

