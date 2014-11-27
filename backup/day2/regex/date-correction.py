#!/usr/bin/env python
import fileinput
import re

for line in fileinput.input(inplace=True, backup='.bak'):
    print re.sub('([0-9]{2})-([0-9]{2})-([0-9]{4})', \
		 r'\2-\1-\3', line),

