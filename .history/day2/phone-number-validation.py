#!/usr/bin/env python
from sys import argv
import re

for line  in open(argv[1]):
    if re.search(r'\b\d{3}[\ \-]?\d{3}[\ \-]?\d{4}\b', line, flags=re.I):
	print line,
