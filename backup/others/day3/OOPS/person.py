#!/usr/bin/env python

class Person(object):
    def __init__(self, first_name, last_name, age, gender):
	self.first_name =  first_name
	self.last_name = last_name
	self.age = age
	self.gender = gender

    def getPerson(self):
	print 'first name : %s' % self.first_name
	print 'last name  : %s' % self.last_name
	print 'age        : %s' % self.age
	print 'gender     : %s' % self.gender


if __name__ == '__main__':
   p = Person('paul', 'allen', 44, 'male')
   p.getPerson()
