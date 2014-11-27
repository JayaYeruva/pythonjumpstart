#!/usr/bin/env python
import os
import sys
from sys import argv
from re import split

class change_ownership(object):
    def __init__(self, uid, gid, path):
	self.uid = uid
        self.gid = gid 
	self.path = path
	self.__is_root()

	if uid.isalpha():
	    self.__get_uid()
	    
	if gid.isalpha():
	    self.__get_gid()
	
        os.chown(path, self.uid, self.gid)

    def __is_root(self):
	if os.getuid() != 0:
	    print >>sys.stderr, \
		  "%s: you must be root to run this" % argv[0]
	    exit(1)

    def __get_uid(self):
	from pwd import getpwnam
	self.uid = getpwnam(self.uid).pw_uid

    def __get_gid(self):
	from grp import getgrnam
	self.gid = getgrnam(self.gid).gr_gid

if __name__ == '__main__':

    uid, gid =  split('[:,]', argv[1]) 
    path = argv[2]
    change_ownership(uid, gid, path)
