#!/usr/bin/env python
import os
import pwd
import grp

class Chown(object):
    def __init__(self, usrname, grpname, path):
	self.uid = self.__get_uid(usrname)
	self.gid = self.__get_gid(grpname)
	self.path = path
	
    def __get_uid(self, usrname):
	return pwd.getpwnam(usrname).pw_uid

    def __get_gid(self, grpname):
	return grp.getgrnam(grpname).gr_gid
   
    def __check4root(self):
	return True if os.getuid() == 0 else False

    def change(self):
	if not self.__check4root():
	    print "%s: you must be root to run this" % sys.argv[0]
	    exit(1)
	os.chown(self.path, self.uid, self.gid) 

if __name__ == '__main__':
    import sys
    usrname, grpname = sys.argv[1].split(':') 
    ch = Chown(usrname, grpname, sys.argv[2])
    ch.change()
 
