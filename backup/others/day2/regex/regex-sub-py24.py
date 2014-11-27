#!/usr/bin/env python
import re
s ='the perl and the perl scripting and the peRl'
c = re.compile('perl', re.I)

print c.sub('python', s)  

