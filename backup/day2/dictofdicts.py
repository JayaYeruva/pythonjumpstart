#!/usr/bin/env python
from pprint import pprint 

keys = ['password', 'uid', 'gid', 'gecos', 'dir', 'shell']
content = {}

with open('/etc/passwd') as fp:
    for line in fp:
	temp = line.rstrip().split(':')
        content[temp[0]] = dict( zip(keys, temp[1:]) )

for login in content:
    print "%16s  %8s  %16s" % \
      (login, content[login]['uid'], content[login]['shell'])
        
