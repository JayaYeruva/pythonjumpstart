#!/usr/bin/env python

s = raw_input('Enter the string ')
lc = {}

for char in s:
   lc[char] = s.count(char)

for char in lc:
    print "%s : %s" % (char, lc[char]) 
