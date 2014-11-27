#!/usr/bin/env python
from person import Person

class Employee(Person):

  def __init__(self, name, age, gender, designation, department):
    super(Employee, self).__init__(name, age, gender)
    self.designation = designation
    self.department = department


  def getInfo(self):
     super(Employee, self).getInfo()
     print "Designation : %s " % self.designation
     print "Department  : %s " % self.department

  

if __name__ == '__main__':
  e = Employee('partric', 34, 'male', 'manager', 'sales')
  e.getInfo()
    
