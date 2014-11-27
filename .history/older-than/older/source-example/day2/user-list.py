#!/usr/bin/env python

users = [ line.split(':')[0] for line in open('/etc/passwd') if '#' not in line  and '!' in line ]

users.sort()

for (i, n) in enumerate(users):
    print i, ":", n
