#!/usr/bin/env python
import sys

def copyall(*files):
   target = files[-1]
   with open(target, 'w') as fw:
        for filename in files[:-1]:
	    with open(filename) as fp:
		fw.write(fp.name.center(60, '-') + "\n")
		for line in fp:
		    fw.write(line)
	        print "%s : file copied " % fp.name
		fw.write('-'.center(60, '-')+"\n")
                fw.write("\n")
                
def usage():
    if len(sys.argv) < 3:
        print "Usage : "
	print "%s source [source ....] target" % sys.argv[0]
        exit(1)

usage()
copyall(*sys.argv[1:]) 
