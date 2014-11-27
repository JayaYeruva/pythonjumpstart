#!/usr/bin/env python
from sys import  argv

def usage():
    print 'Usage:'
    print "%s filenames [filename, ...]" % argv[0]
    exit(1)

def copyall(*files):
    with open(files[-1], 'w') as fw:
	for fname in files[:-1]:
	    with open(fname) as fp:
	        fw.write(fname.center(60, '-') + '\n')
                fw.write(fp.read())
	        fw.write('-'.center(60, '-') + '\n')

if len(argv) < 4:
    print "%s: insufficient arguments" % argv[0]
    usage()

copyall(*argv[1:])
