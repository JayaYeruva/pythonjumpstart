#!/usr/bin/env python
import math

radius = raw_input('enter the radius :')
radius = float(radius)
area = math.pi * (radius ** 2)

print "Area : ", area
print "Area : %.3f" % area
print "Radius %f Area : %.3f" % (radius, area)
