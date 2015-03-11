__author__ = 'ravi'
import math

radius = float(raw_input('Enter the radius :'))

area = math.pi * (radius ** 2)

"""
string formatter  %
"""
content = "radius : %f\narea : %.3f " % (radius, area)

print content

