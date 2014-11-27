#!/usr/bin/env python
import re

#match
s = 'the python scripting and the python'

m = re.search('pYthon', s, re.I)
print m; print 
if m:
    print m.start()
    print m.end()
    print m.span()
    print m.group()

