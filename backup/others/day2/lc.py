#!/usr/bin/env python 
from pprint import pprint
s = 'apple'
lc = {}

for char in s:
    lc[char] = lc.get(char, 0) + 1


for char in lc:
    print "%s : %s" % (char, lc.get(char))

