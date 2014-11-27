#!/usr/bin/env python

mat = [ [1,2,3], 
	[4,5,6, 'x'], 
	[7,8,9]]

#print [ row[1] for row in mat]

res = [ col for row in mat if len(row)==3 \
			for col in row if col%2 ]

print res 
