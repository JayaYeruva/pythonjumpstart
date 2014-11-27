#!/usr/bin/env python
from sys import argv, stderr

def usage():
    print >>stderr, 'Usage:'
    print >>stderr, "%s source-file dest-file" % (argv[0])
    exit(1)

if len(argv) != 3:
    usage()

with open(argv[-1], 'w') as fw:
    fw.writelines( open(argv[-2]).readlines()[::-1] )
    
