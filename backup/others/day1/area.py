#!/usr/bin/env python
from math import pi
radius = input('Enter the radius :')

area = pi * (radius ** 2)

#string formatting
result =  "Radius :%f, Area :%.3f" % (radius, area)  
print result

