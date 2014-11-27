#!/usr/bin/env python

#with  , context manager : gives a scope 

with open('/etc/passwd', 'r') as fp:
    for line in fp:
	print line,
