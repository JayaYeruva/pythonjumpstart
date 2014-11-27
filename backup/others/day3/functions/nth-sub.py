#!/usr/bin/env python

import re
counter = 0

def replace(m):
    global counter
    counter += 1
    #return 'python' if counter==2 else m.group()
    if counter==2:
 	return 'python'
    else:
	return m.group()

s = 'the perl and the perl script and the perl scripting'

print re.sub('perl', replace, s)
