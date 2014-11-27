#!/usr/bin/env python
import os
from sys import argv

class Utils(object):
   
    def lsiNode(self, path):
        if path:
	    self.path = path
        else:
	    self.path = '.'
	for file in os.listdir(self.path):
	    print "%s %s" % (os.stat(self.path+'/'+file).st_ino, file)


if __name__ == '__main__':
    fs = Utils()
    path = None
    if len(argv) > 1:
	path = argv[1]
    fs.lsiNode(path)   
