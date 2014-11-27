#!/usr/bin/env python
s = 'apple'
lc = {}

for char in s:
    lc[char] = lc.get(char, 0) + 1

chars = lc.keys()
chars.sort()
for char in chars:
    print "%s : %s" % (char, lc[char])
