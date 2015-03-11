__author__ = 'ravi'
import re

s = 'the python and the perl scripting'

m = re.match('PythoN', s, re.I)

if m:
    print m
else:
    print "fails to match"
