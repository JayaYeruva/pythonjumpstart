#!/usr/bin/env python

from math import pi
radius = input('Enter the radius :')

area = pi * (radius ** 2)


#string formating 

print 'radius : {}\narea : {:.3f}'.format(radius, area)
content =  'radius : {1}\narea : {1:.3f}'.format(radius, area)
#the above one is for 2.6

print content.upper()

