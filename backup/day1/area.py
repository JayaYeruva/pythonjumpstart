#!/usr/bin/env python
from  math import pi

radius = input('Enter the radius : ')
area = pi * radius ** 2

result = 'Radius : %f\nArea : %.3f' % (radius, area)

print result
