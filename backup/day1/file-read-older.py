#!/usr/bin/env python

fp = open('/etc/passwd')
for line in fp:
    print line.rstrip()
fp.close()
