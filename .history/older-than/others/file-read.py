#!/usr/bin/python

fp = open('/etc/passwd', 'r')
for line in fp:
    print line,
fp.close()
