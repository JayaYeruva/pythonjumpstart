#!/usr/bin/env python
import random
n = random.randint(1, 1000)
i = 1

while i<= 10:
    if i == 1:
	print "one"
    elif i ==2:
	print "two"
    elif i == 3:
	print "three"
    elif i == 5:
	i += 1
	continue
    elif i == 7:
	break
    else: 
        print i
    i += 1 
