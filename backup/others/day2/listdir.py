#!/usr/bin/env python

from sys import argv
import os
from os.path import isdir, isfile

path = '.'
if  len(argv) == 2:
    path = argv[-1]

for name in os.listdir(path):
    abs_path = "%s/%s" % (path, name)
    if isdir(abs_path):
	print "%22s  directory" % name
    elif isfile(abs_path):
	print "%22s  regualr" % name
