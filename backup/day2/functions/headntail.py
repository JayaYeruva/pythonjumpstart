#!/usr/bin/env python

def headntail(filename, **param):
    count = param.get('count', 10)
    order = param.get('order', 'head')
    if order == 'head':
	content = open(filename).readlines()[:count]
    elif order == 'tail':
	content = open(filename).readlines()[-count:]
    return ''.join(content)

print headntail('/etc/passwd', order='tail', count=5),
