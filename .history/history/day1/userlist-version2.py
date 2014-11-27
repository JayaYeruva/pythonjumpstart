#!/usr/bin/env python
from pprint import pprint
users = []

with open('/etc/passwd') as fp:
    for line in fp:
        users.append( line.split(':')[0].title() )

users.sort()

for ind, name in enumerate(users, 1):
    print "%6s  %s" % (ind, name)
