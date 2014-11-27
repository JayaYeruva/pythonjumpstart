#!/usr/bin/env python
import re
s ='the perl and the perl scripting and the peRl'

print re.sub('perl', 'python', s, flags=re.I) 

