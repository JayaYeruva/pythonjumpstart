#!/usr/bin/env python
import sys
import re

with open(sys.argv[1], 'r') as fp:
  for ln in fp:
    ln = ln.rstrip()
    print re.sub(r'([0-9]{2})-([0-9]{2})-([0-9]{4})', r'\3-\2-\1',    ln)
