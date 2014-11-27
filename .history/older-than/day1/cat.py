#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    print "Usage :"
    print "%s filename" % sys.argv[0]
    exit(1)

with open(sys.argv[1])  as  fp:
   for line in fp:
	print line.rstrip()
