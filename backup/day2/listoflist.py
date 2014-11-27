#!/usr/bin/env python
from pprint import pprint

content = [ line.rstrip().split(":") \
		for line in open('/etc/passwd') ]

def sortit(item):
    return item[0]

content.sort(key=sortit, reverse=True)

pprint(content)
#for row in content:
#    print "%16s  %16s" % (row[0], row[-1])
