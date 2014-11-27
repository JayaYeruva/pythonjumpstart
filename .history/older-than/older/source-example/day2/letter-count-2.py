#!/usr/bin/env python
s = raw_input('Enter the string :')
lc = {}

for char in s:
    if not lc.has_key(char):
        lc[char] = s.count(char)

for char in  lc.keys():
   print "%s : %s" % (char, lc[char])
