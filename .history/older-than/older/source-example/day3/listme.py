#!/usr/bin/env python
import sys
import os
import stat
import glob
import time

for f_nam in glob.glob(sys.argv[1]):
    stat_res = os.stat(f_nam)
    if stat.S_ISREG(stat_res.st_mode):
       print "%s : regular file Modified At: %s " % ( f_nam, \
		time.ctime(stat_res.st_mtime))
    elif stat.S_ISDIR( stat_res.st_mode): 
       print "%s : dir spl  file" % f_nam
    
       
