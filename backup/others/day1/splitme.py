#!/usr/bin/env python

s = 'root:x:0:0:root:/root:/bin/bash'
#row = (s.split(':'))[0]
row = s.split(':')

print row

s_from_list = ','.join(row)

print s_from_list

