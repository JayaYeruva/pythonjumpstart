#!/usr/bin/env python
from pprint import pprint 

keys = ['login', 'password', 'uid', 'gid', 'gecos', 
	'dir', 'shell']

content = [ dict(zip(keys, line.rstrip().split(':'))) \
		       for line in open('/etc/passwd') ]

for row in content:
     print "%16s  %16s" % (row['login'], row['shell'])
