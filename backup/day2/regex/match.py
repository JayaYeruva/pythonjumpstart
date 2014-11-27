#!/usr/bin/env python 
import re

s = 'the perl and the python scripting'
m = re.match('PerL', s, re.I)

if m:
    print m
else:
    print "failed to match"   
