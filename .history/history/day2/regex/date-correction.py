#!/usr/bin/env python
import sys
import re

with open(sys.argv[1]) as fp:
    for line in fp:
	print re.sub(r'(\d\d)-(\d\d)-(\d\d\d\d)', r'\3-\1-\2', line, flags=re.I),

