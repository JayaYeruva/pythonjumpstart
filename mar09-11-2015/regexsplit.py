__author__ = 'ravi'
import re

s = 'root,x;0-0:root,/root|/bin/bash'

l = re.split('[,;\-:|]', s)

for item in l:
    print item