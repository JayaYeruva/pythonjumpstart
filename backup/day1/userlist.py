#!/usr/bin/env python
userlist = []

with open('/etc/passwd') as fp:
    for line in fp:
	userlist.append( line.split(':')[0].upper())

userlist.sort()

with open('userlist.dat', 'w') as fw:
    for ln, login in enumerate(userlist, 1):
         print "%6s  %s" % (ln, login)
         fw.write("%6s  %s\n" % (ln, login))


