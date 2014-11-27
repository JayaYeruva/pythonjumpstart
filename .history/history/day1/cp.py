#!/usr/bin/env python
from sys import argv

def usage():
    print "%s: missing file operand" % argv[0]
    print "Usage :"
    print "%s source-file dest-file" % argv[0]
    exit(1) 
 
if len(argv) != 3:
    usage()

with open(argv[1]) as fp:
    with open(argv[2], 'w') as fw:
        fw.write( fp.read() )


