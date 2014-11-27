#!/usr/bin/env python
import re
s = 'root:x:0:0:root:/root:/bin/bash'

def put_bracket(m):
    return "[%s]" %  m.groups()[0].upper()

print re.sub('([AEIOU])', put_bracket, s, flags=re.I)

