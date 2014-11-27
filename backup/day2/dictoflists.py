#!/usr/bin/env python
from pprint import pprint 

content = {}

with open('/etc/passwd') as fp:
    for line in fp:
	temp = line.rstrip().split(':')
        content[temp[0]] = temp[1:]

for login in content:
     print "%16s  %8s  %16s" % \
		(login , content[login][1], content[login][-1]) 

        
