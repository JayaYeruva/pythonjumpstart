#!/usr/bin/env python

import math 
radius = 3.152
area = math.pi * (radius ** 2) 

name = 'jimmy'
gender = 'male'
age = 45

print name, 
print gender,
print age
print name, gender, age
value =  name +','+gender +','+str(age)
print value 
result = "radius : %f, area :%.3f" % (radius, area)   #formatter  %

print result 

value = "%s,%s,%d\n" % (name,gender,age)
print value





