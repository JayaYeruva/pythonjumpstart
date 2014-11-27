#!/usr/bin/env python

class Person(object):
    def __init__(self, first_name, last_name, age, \
				gender=None):
        self.__first_name = first_name
	self.__last_name  = last_name
	self.__age	= age
	self.__gender	= gender

    def __get_person(self):  #private method
	for attr in  sorted(self.__dict__.keys()):
	    print "%s : %s" % (attr, self.__dict__[attr])
  
    def get_wrap_person(self):
	self.__get_person()

if __name__ == '__main__':
    p = Person('allen', 'paul', 3)
    p.get_wrap_person()



