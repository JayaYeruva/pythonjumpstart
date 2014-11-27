#!/usr/bin/env python
from sys import argv
import re

for line  in open(argv[1]):
    m = re.search(r'\b(\d)(\d)\.\2\1\b', line, flags=re.I)
    if m:
        print m.groups()
	print line,
