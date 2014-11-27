#!/usr/bin/env python
from sys import argv
from pprint  import pprint

content = open(argv[1]).readlines()
print '|'.join(content[::-1]),
#for line in content[::-1]:
#    print line,
