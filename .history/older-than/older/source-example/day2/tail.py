#!/usr/bin/env python
import sys

try:
  with open(sys.argv[1]) as fp:
     with open(sys.argv[2], 'w') as fw:
        for line in fp.readlines()[-10:] :
            print line.rstrip()
            fw.write( line )
except IOError, e:
   print "%s : %s" % (sys.argv[0],  e)
   exit(1)
