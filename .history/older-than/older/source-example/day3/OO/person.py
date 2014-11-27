#!/usr/bin/env python

class Person (object):
   def __init__(self, nam, gen):  #constructor
	self.__name = nam
        self.gender = gen

   def getPerson(self):
        print "Name : %s " % self.__name
        print "Gender : %s " % self.gender

   def __del__(self):  #destructor 
	print "%s : destroying....." %  self 
  
p1 = Person('kimberly', 'female')
p1.getPerson()
print p1.__name
