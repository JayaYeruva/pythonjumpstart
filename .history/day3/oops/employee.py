#!/usr/bin/env python
from person import Person

class Employee(Person):
    def __init__(self, eid, firstName, lastName, age, gender,\
		 designation, department):
	self.eid = eid
	super(Employee, self).__init__(firstName, lastName, \
		age, gender) #calling the base class constructor
        self.designation = designation
	self.department = department

    def getEmployee(self):
	print "employee id : %s" % self.eid
        self.getPerson()
	print "Designation : %s" % self.designation
	print "Department : %s" % self.department

if __name__ == '__main__':
    e = Employee('1001', 'henry', 'jacob', 12, 'male', \
		'manager', 'sales')
    e.getEmployee()

   
