#!/usr/bin/env python
import re

#match
s = 'the python scripting and the python the snake'

for m in re.finditer('pYthon', s, re.I):
    print m.start()
    print m.end()
    print m.span()
    print m.group()
    print;print

