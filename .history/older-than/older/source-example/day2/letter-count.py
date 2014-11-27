#!/usr/bin/env python
s = raw_input('Enter the string :')
lc = {}

for char in s:
   if lc.has_key(char):
	lc[char] += 1
   else:
        lc[char] = 1

chars = lc.keys()
chars.sort()

for ch in chars:
   print "%s : %s" %(ch, lc[ch])

#for (k, v) in  lc.items():
#   print "%s : %s" % (k, v)
