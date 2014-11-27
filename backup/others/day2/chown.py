#!/usr/bin/env python
from pwd import getpwnam
from grp import getgrnam
from re import split
from os import chown, getuid
from sys import argv, stderr

def check4root():
    if getuid() != 0 :
	print >>stderr, '%s: you must be a root' % argv[0]	
	exit(1)

check4root()

#chown user:/.group filename
uid, gid = split('[:.]',  argv.pop(1))

if uid.isalpha():
    #uid = getpwnam(uid).pw_uid
    uid = getpwnam(uid)[2]

if gid.isalpha():
    #gid = getgrnam(gid).gr_gid
    gid = getgrnam(gid)[2]

chown(argv[-1], uid, gid)    

 
