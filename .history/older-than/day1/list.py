#!/usr/bin/env python

l = ['perl', 'larry wall', 'ruby', 'matz' , 'python', 'rosvassum']

toupper = map(str.upper, l)
for index, value in enumerate(toupper):
   print "%s : %s "% (index, value)
