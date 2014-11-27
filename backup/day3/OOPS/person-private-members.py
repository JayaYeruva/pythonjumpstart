#!/usr/bin/env python

class Person(object):
    def __init__(self, first_name, last_name, age, \
				gender=None):
        self.__first_name = first_name
	self.__last_name  = last_name
	self.__age	= age
	self.__gender	= gender

    def get_person(self):
	print "First Name : %s" % self.__first_name
	print "Last Name : %s" % self.__last_name
	print "Age : %s" % self.__age
	print "Gender : %s" % self.__gender 

if __name__ == '__main__':
    p = Person('allen', 'paul', 3)
    print p._Person__first_name
    print p.__dict__

