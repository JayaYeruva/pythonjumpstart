#!/usr/bin/env python

mat = [[1,2,3], [4,5,6], [7,8,9]]
mat[1][1] = 'x'
mat[-1].append(0)

for row in mat:
   for col in row:
	print col, "\t",
   print
