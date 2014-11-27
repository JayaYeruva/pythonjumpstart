#!/usr/bin/env python

l = [1,2,3,4,5]
res = []
for item in l:
    res.append(item ** item)

print res

res2 = [ i**i for i in l]  #list comp.
print res2
print l
