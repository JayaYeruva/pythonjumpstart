#!/usr/bin/env python
import re
from fileinput import input

for line in input(inplace=1, backup='.bakup'):
    print re.sub('([0-9]{2})-([0-9]{2})-([0-9]{4})', r'\2-\1-\3', line),  
