#!/usr/bin/env python
from sys import argv
import re

for line  in open(argv[1]):
    m = re.search(r'\d\d\d\d*', line, flags=re.I)
    if m:
        if int(m.group()) >= 100:
	    print line,
