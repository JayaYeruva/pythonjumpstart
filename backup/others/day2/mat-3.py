#!/usr/bin/env python
from pprint import pprint
mat = [[1,2,3], [4,5,6], [7,8,9]]

res = [ c for r in mat for c in r  if c%2 ]
pprint(res)
