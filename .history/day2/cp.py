#!/usr/bin/env python
from sys import argv

def usage():
    print "Usage:"
    print "%s source-file dest-file" % argv[0]
    exit(1)

if len(argv) != 3:
    usage()

with open(argv[2], 'w') as fw:
    for line in open(argv[1]):
        fw.write(line)

print '1. file copied'
