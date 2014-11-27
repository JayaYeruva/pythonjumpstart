#!/usr/bin/env python

users = [line.split(':')[0] for line in open('/etc/passwd')]
groups = [line.split(':')[0] for line in open('/etc/group')]


u = set(users)
g = set(groups)

#print u.intersection(g)
#print u.union(g)

#print u.difference(g)
print g.difference(u)
