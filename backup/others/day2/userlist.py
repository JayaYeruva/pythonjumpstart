#!/usr/bin/env python
from pprint import pprint

def sortit(a, b):
    return cmp(a[0], b[0])

content = []

fp = open('/etc/passwd')
for line in fp:
    content.append( line.rstrip().split(':') )

fp.close()

content.sort(cmp=sortit)

for row in content:
    print "%22s  %18s" % (row[0], row[-1])

#pprint(content)
