#!/usr/bin/env python
# comment 
info = [1, 'peter', 'manager', 'sales', 45000.99]
#info.append('20%')

i = info.index('peter')

info.insert(i+1, 'pan')
info.sort(reverse=True)  
#info.reverse()
for (index, value) in enumerate(info):
   print "[%d] -> %s " % (index, info[index])

