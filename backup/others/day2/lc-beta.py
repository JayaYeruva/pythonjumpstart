#!/usr/bin/env python 
from pprint import pprint
s = 'apple'
lc = {}

for char in s:
    if lc.has_key(char):
	lc[char] += 1   
    else:
	lc[char] = 1   


for char in lc:
    print "%s : %s" % (char, lc.get(char))

print;print 

pprint(lc)
