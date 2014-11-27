#!/usr/bin/env python
from pprint import pprint
users = []

with open('/etc/passwd') as fp:
    for line in fp:
        users.append( line.split(':')[0].title() )

users.sort()

i = 1
for name in users:
    print "%6s  %s" % (i, name)
    i += 1
