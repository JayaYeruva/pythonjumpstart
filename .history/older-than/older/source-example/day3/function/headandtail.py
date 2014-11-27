#!/usr/bin/env python
import sys
def ht(**args):
    order = 'head'
    line_no = 10
    if not args.has_key('filename'):
	print "%s : ht: expects keyword filename" % sys.argv[0]
	exit(1)
    
    if args.has_key('line_num'):
	line_no = args['line_num']    
       
    if args.has_key('order'):
        order = args['order']

    with open(args['filename']) as fp:
	if order == 'head':
            return fp.readlines()[:line_no]
	elif order  == 'tail':
            return fp.readlines()[-(line_no):]

print "".join( ht(filename='/etc/passwd', line_num=3, order='tail'))
#print "".join( ht(filename='/etc/passwd', order='head', line_num=5))
