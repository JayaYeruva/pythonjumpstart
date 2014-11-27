#!/usr/bin/env python
from person import Person

class Employee(Person):
    def __init__(self, eid, first_name, last_name, age, \
		gender, designation, department):
	self.eid  = eid
	self.designation = designation
	self.department = department
	super(Employee, self).__init__(first_name, last_name, age, gender)

    def get_info(self):
	print "Employee id : %s" % self.eid
	super(Employee, self).get_info() #base version get_info
	print "Department : %s" % self.department
	print "Designation : %s" % self.designation

if __name__ == '__main__':
    e = Employee(101, 'tim', 'joe', 4, 'male', 'clerk', 'sale')
    e.get_info()
