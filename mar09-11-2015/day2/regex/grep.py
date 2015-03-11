__author__ = 'ravi'
import re
from fileinput import input
from sys import argv

cmp_pattern = re.compile(argv.pop(1), re.I)

for line in input():
    m = cmp_pattern.search(line)
    if m:
        print m.group()
        #print line.rstrip()
