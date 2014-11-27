#!/usr/bin/env python
from re import finditer

s = 'the perl and the perl scripting'

for m in finditer('perl', s):
    print m.group()
    print s[:m.start()]
    print s[m.end():]; print

