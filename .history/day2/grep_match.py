#!/usr/bin/env python
from sys import argv
import re

for line  in open(argv[2]):
    if re.search(argv[1], line, flags=re.I):
	print line,
