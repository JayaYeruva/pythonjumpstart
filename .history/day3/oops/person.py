#!/usr/bin/env python

class Person(object):
    def __init__(self, firstName, lastName, age=None, gender=None):
	self.firstName = firstName
 	self.lastName = lastName
	if age:
	    self.age = age
	if gender:
	    self.gender = gender

    def getPerson(self):
	print "first name : %s" % self.firstName
	print "last name : %s" % self.lastName
        if self.__dict__.get('age'):
	    print "age : %s" % self.age
        if self.__dict__.get('gender'):
	    print "gender : %s" % self.gender

if __name__ == '__main__':
    p = Person('paul', 'allen')
    p.getPerson()
    print __name__
