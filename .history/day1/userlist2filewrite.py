#!/usr/bin/env python

usernames = []

#with open('/etc/passwd') as fp:
for line in open('/etc/passwd'):
        usernames.append(line.split(':')[0].upper())

usernames.sort()

with open('userlist.dat', 'w') as fw:
    for (ind, name) in enumerate(usernames, 1):
         print "%6s  %s" % (ind, name)
         fw.write( "%6s  %s\n" % (ind, name) )

