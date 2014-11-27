#!/usr/bin/env python

s = 'a sample string'
lookup = {}

for char in s:
   if lookup.has_key(char):
	lookup[char] += 1
   else:
	lookup[char] = 1


chars = lookup.keys()
chars.sort()

for char in chars:
    print "%s : %s" % (char, lookup[char])
