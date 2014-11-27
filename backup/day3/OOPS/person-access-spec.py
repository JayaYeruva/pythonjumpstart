#!/usr/bin/env python

class Person(object):
    def __init__(self, first_name, last_name, age, \
				gender=None):
        self.first_name = first_name
	self.last_name  = last_name
	self.age	= age
	self.gender	= gender

    def get_person(self):
	for attr in  sorted(self.__dict__.keys()):
	    print "%s : %s" % (attr, self.__dict__[attr])

if __name__ == '__main__':
    p = Person('allen', 'paul', 3)
    p.address = '49 mg road'
    #print p.first_name
    #print p.age
    #print p.gender
    p.get_person()



