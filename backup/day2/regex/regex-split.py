#!/usr/bin/env python
import re
s = 'root:x;0,0-root:/root,/bin/bash'

for item in re.split('[;,\-:]', s):
    print item

