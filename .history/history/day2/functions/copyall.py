#!/usr/bin/env python
import sys

def copyall(*args):
    with open(args[-1], 'w') as fw:
        for filename in args[:-1]:
	    fw.write("%s\n" % filename.center(60, '-'))
	    with open(filename) as fp:
		fw.write(fp.read())
	    fw.write("%s\n" % '-'.center(60, '-'))

copyall(*sys.argv[1:])  
