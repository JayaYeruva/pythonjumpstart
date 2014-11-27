#!/usr/bin/env python

i = 1

while i <= 10:
    if i == 7:
	break
    elif i == 1:
	print 'i' 
    elif i == 2:
	print 'ii'
    elif i == 3:
	print 'three'
    elif i == 5:
        i += 1
        continue
    else: 
        print i
    i += 1
