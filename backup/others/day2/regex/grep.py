#!/usr/bin/env python
from sys import argv
from fileinput import input 
import re

pattern = argv.pop(1)

for line in input():
    if re.search(pattern, line, re.I):
	print line,
