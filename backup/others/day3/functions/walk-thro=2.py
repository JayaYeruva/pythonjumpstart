#!/usr/bin/env python

from  os.path import walk

def select_files(args, dirname, files):

    pdfs = [ filename for filename in files if filename.endswith(args) ]
    if len(pdfs):	
        print dirname
	for pdf_file in pdfs:
            print "\t%s" % pdf_file
        print;print

walk('/home/ravi/Training', select_files, '.pdf')
