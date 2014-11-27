#!/usr/bin/env python
import sys
import re

with open(sys.argv[2], 'r') as fp:
    for line in fp:
        if re.search(sys.argv[1], line, re.I):
	    print line.rstrip()
