#!/usr/bin/env python
gender = {}
dept = []
with open('emp.dat', 'r') as fp:
    for line in fp:
        row = line.split(',')
        if gender.has_key(row[1]):
	    gender[row[1]] += 1
        else:
	    gender[row[1]] = 1

        if not row[3] in dept:
	   dept.append(row[3])

g_k = gender.keys()
g_k.sort()
for key in g_k:
    print "%s : %s" % (key, gender[key])
print; print

for d in dept:
    print d

