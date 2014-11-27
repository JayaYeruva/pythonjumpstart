#!/usr/bin/env python

from person import Person

class Employee(Person):
    def __init__(self, eid, first_name, last_name, age, gender, 
		designation, department):
	self.eid = eid
        super(Employee, self).__init__(first_name, last_name, age, gender)
	#the above line calls the base class constructor

	self.designation = designation
	self.department = department

    def getEmployee(self):
	print "id 	:  %s" % self.eid 
        self.getPerson()
	print "designation 	:  %s" % self.designation 
	print "department 	:  %s" % self.department 

if __name__ == '__main__':
    e = Employee(1001, 'steve', 'jane', 4, 'male', 'manager', 'ops')
    e.getEmployee()
