#!/usr/bin/env python
#from pprint import pprint

users = []
fw = open('userlist.dat', 'w')

fp = open('/etc/passwd')
for line in fp:
    users.append( (line.split(':'))[0].title() )

users.sort()   


for ln, user in enumerate(users, 1):
    print "%6s  %s" % (ln, user)
    fw.write("%6s  %s\n" % (ln, user))

fp.close()
fw.close()

