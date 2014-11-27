#!/usr/bin/env python

class Car (object):
  def __init__(self):
    if self.__class__ == Car:
	raise NotImplementedError, "%s : an abstract class can't be instantiated" % \
					self.__class__.__name__
 

class Sedan(Car):
   
   pass

if __name__ == '__main__':
  car = Sedan()
