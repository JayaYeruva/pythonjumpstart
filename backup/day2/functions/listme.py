#!/usr/bin/env python
import os
import os.path
from pprint import pprint

def listme(dir_path='.'):
    files = []
    dirs = []

    for file_item in  os.listdir(dir_path):
	path = dir_path+'/'+file_item

	if os.path.isfile(path):
	    files.append(path)   
	if os.path.isdir(path):
	    dirs.append(path)   

    return(files, dirs)


pprint( listme('/home/ravi') )
