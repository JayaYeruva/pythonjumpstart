#!/usr/bin/env python
from sys import argv
from re import search, I
from fileinput import input

pattern = argv.pop(1)

for line in input():
    if search(pattern, line, I):
	print line, 

