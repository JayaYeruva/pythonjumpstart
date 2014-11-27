#!/usr/bin/env python

class Box(object):
  def __init__(self, side):
     self.side = side
  
  def __str__(self):
	return "<%s: side:%s>" % (self.__class__.__name__, self.side)

  def __add__(self, other):
	return Box(self.side + other.side)

if __name__ == '__main__':
    b1 = Box(10)
    b2 = Box(20)
    b3 = b1 + b2 
    print b3
