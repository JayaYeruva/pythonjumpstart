#!/usr/bin/env python
from math import ceil

def center(string, width=60, fill=' '):
    if width <= len(string) :
	return string
    ntimes = (width-len(string))/2.0
    return fill * int(ceil(ntimes)) + string + fill * int(ntimes) 

print center('perl', 2)
print center('perl', 7, '-')

print center('perl', fill='*')
