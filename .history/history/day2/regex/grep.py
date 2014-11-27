#!/usr/bin/env python
from sys import argv
from re import search
import re

with open(argv[2]) as fp:
    for line in fp:
        if search(argv[1], line, re.I):
	    print line,
