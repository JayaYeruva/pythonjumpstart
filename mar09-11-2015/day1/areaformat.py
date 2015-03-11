__author__ = 'ravi'
import math

radius = float(raw_input('Enter the radius :'))

area = math.pi * (radius ** 2)


'''
{index:format}
'''


print "radius : {}\narea : {:.3f}".format(radius, area)
