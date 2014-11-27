#!/usr/bin/env python
from math import pi
radius = input('enter the radius :')
area = pi * (radius ** 2 )

result =  "Radius : %f, Area : %.3f" % (radius, area)  #()  tuple

print result
