#!/usr/bin/env python

s = 'root:x:0:0:root:/root:/bin/bash'
l = s.split(':')
print l[0]
content = l[1:]

s = '|'.join(content)
print s
