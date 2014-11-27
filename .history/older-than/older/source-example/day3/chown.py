#!/usr/bin/env python
import os
import pwd
import grp
import sys 

if 0 != os.getuid():
    print "%s : you must to be a root" % sys.argv[0]
    exit(1)

# username:grpname
ids = None
uid = None
gid = None
if ':' in sys.argv[1]:
     ids = sys.argv[1].split(':')
     uid = pwd.getpwnam(ids[0]).pw_uid
     gid = grp.getgrnam(ids[1]).gr_gid
else:
     uid = pwd.getpwnam(sys.argv[1]).pw_uid
     gid = os.stat(sys.argv[2]).st_gid
os.chown(sys.argv[2], uid, gid)

