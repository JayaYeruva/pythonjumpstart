#!/usr/bin/env python

class Person(object):
    def __init__(self, first_name, last_name, age, gender):
	self.first_name = first_name
	self.last_name = last_name
        self.age = age
	self.gender = gender

    def get_person(self):
	print "first name : %s" % self.first_name
	print "last name : %s" % self.last_name
	print "age : %s" % self.age
	print "gender : %s" % self.gender

class Employee(Person):
    def __init__(self, eid, first_name, last_name, age, gender, desg, dept):
	self.eid = eid
	super(Employee, self).__init__(first_name, last_name, age, gender)
	#the above statement calls the base class constructor
        self.desg = desg
        self.dept = dept

    def get_employee(self):
	print 'employee id : %s' % self.eid
	self.get_person()
        print 'designation : %s'  % self.desg
        print 'department : %s'  % self.dept

if __name__ == '__main__':
    e = Employee('e1001', 'steve', 'allen', '4', 'male', 'clerk', 'sales')
    e.get_employee()
