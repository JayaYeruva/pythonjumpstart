#!/usr/bin/env python
import sys
import re

def help():
  print "Usage : "
  print "%s pattern filename" % sys.argv[0]
  exit(1)

if len(sys.argv) != 3:
   help()

with open(sys.argv[2]) as fp:
  for line in fp:
    if re.search(sys.argv[1], line, re.I):
	print line.rstrip()
  
