#!/usr/bin/env python
import re
pattern = r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})'

ip = '192.168.1.300'

m = re.search(pattern, ip)

if m:
   ip_part =  map( int, m.groups())
   if (1 <= ip_part[0] <= 255)  and (1 <= ip_part[1] <= 255) and \
		(1 <= ip_part[2] <= 255) and (1 <= ip_part[3] <= 255):
	print "%s : valid" % ip


