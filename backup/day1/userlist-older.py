#!/usr/bin/env python
userlist = []

with open('/etc/passwd') as fp:
    for line in fp:
	userlist.append( line.split(':')[0].upper())

userlist.sort()
ln = 1

for login in userlist:
    print "%6s  %s" % (ln, login)
    ln += 1
