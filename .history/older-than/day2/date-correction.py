#!/usr/bin/env python

import sys
import re
pattern = r'(\d{2})-(\d{2})-(\d{4})'

with open(sys.argv[1]) as fp:
  for line in fp:
    print re.sub(pattern, r'\2-\1-\3', line.rstrip())
