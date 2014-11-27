#!/usr/bin/env python 
import re

s = 'the perl and the python scripting'
m = re.search('PerL', s, re.I)

if m:
    print m
    print "matched : %s" % m.group()
    print "start-index :", m.start()
    print "end-index :", m.end()
    print m.span()
else:
    print "failed to match"   
