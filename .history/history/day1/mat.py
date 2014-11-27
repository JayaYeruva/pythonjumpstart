#!/usr/bin/env python

mat = [[1,2,3], [4,5,6], [7,8,9]]

#from pprint import pprint
#pprint(mat)

mat[1][1] = 'x'
mat[2].append(100)

for row in mat:
    for col in row:
         print "%s\t" % col,
    print
