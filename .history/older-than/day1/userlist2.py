#!/usr/bin/env python

userlist = []

with open('/etc/passwd') as fp:
    for line in fp:
        userlist.append( line.split(':')[0].title() )  

userlist.sort()
for i, name in enumerate(userlist):
    print "%5s %s" % ((i+1), name)

