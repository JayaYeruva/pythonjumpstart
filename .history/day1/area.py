#!/usr/bin/env python
#from math import pi
import math
radius = input('enter the radius:')
area = math.pi * (radius ** 2)

res = "Radius : %f, Area : %.3f" % (radius, area)  #string formatting

print res
