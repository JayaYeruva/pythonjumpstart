#!/usr/bin/env python
from sys import argv, exit

def usage():
   if(len(argv)!=3):
	print 'Usage:'
	print '%s source-file dest-file' % argv[0]
	exit(1)

usage()

content = open(argv[-2]).readlines()[::-1]  #[::-1] will reverse the content

fw = open(argv[-1], 'w')

for line in content:
    fw.write(line)

fw.close()

