#!/usr/bin/env python

usernames = []

with open('/etc/passwd') as fp:
    for line in fp:
        usernames.append(line.split(':')[0].upper())

usernames.sort()
counter = 1
for name in usernames:
    print "%6s  %s" % (counter, name)
    counter += 1

