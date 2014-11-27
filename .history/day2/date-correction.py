#!/usr/bin/env python
from sys import argv
import re
for line in open(argv[1]):
    print re.sub(r'(\d{2})-(\d{2})-(\d{4})', r'\3-\1-\2', \
				line, flags=re.I), 
