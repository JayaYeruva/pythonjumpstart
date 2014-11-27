#!/usr/bin/env python

userlist = []

with open('/etc/passwd') as fp:
    for line in fp:
        userlist.append( line.split(':')[0].title() )  

userlist.sort()
i = 1
with open('userlist.dat', 'w') as fw:
    for name in userlist:
        print "%5s %s" % (i, name)
        fw.write( "%5s %s\n" % (i, name) )
        i += 1

