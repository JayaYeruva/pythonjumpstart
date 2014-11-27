#!/usr/bin/env python
fp = open('/etc/passwd')
for line in fp:
    line = line.rstrip()
    print line
fp.close()
