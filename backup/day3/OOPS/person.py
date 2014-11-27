#!/usr/bin/env python

class Person(object):
    def __init__(self, first_name, last_name, age, \
				gender=None):
        self.first_name = first_name
	self.last_name  = last_name
	self.age	= age
	self.gender	= gender

    def get_info(self):
	print "First Name : %s" % self.first_name
	print "Last Name : %s" % self.last_name
	print "Age : %s" % self.age
	print "Gender : %s" % self.gender 

if __name__ == '__main__':
    p = Person('allen', 'paul', 3)
    p.get_info()

