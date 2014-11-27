#!/usr/bin/env python
import re

s = 'root:x:0:0:root:/root:/bin/bash'
print re.sub(':', '|', s)

