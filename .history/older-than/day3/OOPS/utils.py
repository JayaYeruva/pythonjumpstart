#!/usr/bin/env python
import sys
import os
import filecmp
import shutil
import pwd
import grp
class Utils(object):
  def __init__(self):
        pass

  def fileCmp(self, file1, file2):
    return "'%s' and '%s' are %s" % ( file1, file2, " same" \
			if filecmp.cmp(file1, file2) else 'different')
  
  def makeTar(self, a_name, root_dir):
    shutil.make_archive(a_name, 'bztar', root_dir)
	
  def chown(self, filename, user, group):
      if os.getuid() != 0:
	print "%s : your must be root to run this !!!!" % sys.argv[0]
        exit(1)
      uid = pwd.getpwnam(user).pw_uid
      gid = grp.getgrnam(group).gr_gid
      os.chown(filename, uid, gid)

if __name__ == '__main__':
   u  = Utils()
   #print u.fileCmp(sys.argv[1], sys.argv[2])
   #u.makeTar(sys.argv[1], sys.argv[2]) 
   u.chown(sys.argv[1], sys.argv[2], sys.argv[3])
