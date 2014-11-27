#!/usr/bin/env python

from  os.path import walk

def select_files(args, dirname, files):
    first = 1
    for pdf_file in filter(lambda filename: filename.endswith(args), files):
        if first == 1:
  	    first += 1	
	    print dirname
        print "\t%s" % pdf_file
    if first == 2:
       print;print

walk('/home/ravi/Training', select_files, '.pdf')
