#!/usr/bin/env python

s = raw_input('Enter the string ')
lc = {}

for char in s:
   if lc.has_key(char):
	lc[char] += 1
   else:
	lc[char] = 1

for char in lc:
    print "%s : %s" % (char, lc[char]) 
