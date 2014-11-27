#!/usr/bin/env python
import re
count = 0
s = 'root:x:0:0:root:/root:/bin/bash'

def replaceit(m):
    global count
    count += 1
    return '|' if count == 3 else m.groups()[0]

print re.sub('(:)', replaceit, s)

