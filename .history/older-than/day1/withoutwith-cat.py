#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    print "Usage :"
    print "%s filename" % sys.argv[0]
    exit(1)

fp =  open(sys.argv[1])
for line in fp:
    print line
fp.close()
