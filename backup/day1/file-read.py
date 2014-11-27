#!/usr/bin/env python

with open('/etc/passwd') as fp:
    for line in fp:
	print line.rstrip()
