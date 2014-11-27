#!/usr/bin/env python
# comment 
info = [1, 'peter', 'manager', 'sales', 45000.99]

for item in info:
    if type(item) == type(''): 
	print item.upper()
    else:
	print item 

#print type(info)
#print len(info)
#mutable 
info[3] = 'production'
#indexing 
#print info[0]
#print info[1]
#print info[2]
#print info[3]
#print info[-1]

det = info[1:4]
print det 
