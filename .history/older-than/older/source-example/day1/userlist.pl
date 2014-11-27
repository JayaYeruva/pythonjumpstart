#!/usr/bin/env python
import sys
fp = open(sys.argv[1], 'r')
users = []
for line in fp:
    users.append(line.split(':')[0].title())

users.sort()

for (i, n) in enumerate(users):
    i+=1
    print "%5s %s" % (i, n)   
fp.close()
