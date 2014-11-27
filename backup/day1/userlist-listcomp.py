#!/usr/bin/env python
from pprint import pprint
userlist = sorted( [ line.split(':')[0].upper() \
			for line in open('/etc/passwd') ])

#print userlist.sort()
pprint(userlist)
