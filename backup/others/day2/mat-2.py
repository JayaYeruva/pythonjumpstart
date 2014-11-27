#!/usr/bin/env python
from pprint import pprint
mat = [[1,2,3], [4,5,6], [7,8,9]]
#mat[1][1] = 'x'

res = [ r[1] for r in mat]
pprint(res)


