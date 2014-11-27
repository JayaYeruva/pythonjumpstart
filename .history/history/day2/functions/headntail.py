#!/usr/bin/env python

def headntail(**args):
    count = args.get('count', 10)
    order = args.get('order', 'head')
    filename = args.get('file')
    content = '';
    if filename:
	with open(filename) as fp:
            if order == 'head':
	        content = fp.readlines()[:count]
            elif order == 'tail':
	        content = fp.readlines()[-count:]
	return ''.join(content)
     
print headntail(file='/etc/passwd', count=4, order='tail'),
