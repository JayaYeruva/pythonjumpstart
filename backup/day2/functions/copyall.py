#!/usr/bin/env python
from sys import argv

def copyall(*files):
    with open(files[-1], 'w') as fw:
        for file_name in  files[:-1]:
	    fw.write(file_name.center(60, '-')+"\n")
	    fw.write(open(file_name).read())
	    fw.write('-'.center(60, '-')+"\n")

copyall(*argv[1:])

