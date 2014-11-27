#!/usr/bin/env python
from os import listdir 
from sys import argv
import os.path as op
path = '.'

if len(argv) == 2:
    path = argv[1]

for file_name in listdir(path):
    abs_path = path.rstrip('/') + '/' +file_name
    if op.isdir( abs_path ):
	print "%40s: directory" % abs_path
    elif op.isfile( abs_path ):
	print "%40s: regular file" % abs_path
