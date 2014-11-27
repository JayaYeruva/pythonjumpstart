#!/usr/bin/env python

info = {'hostname':'ws1.rootcap.in', 'ipaddr':'132.12.12.1', 
	 'purpose':'workstation', 'platform' : 'linuz2'
	}
info['cpu-core'] = 16

del(info['platform'])

val = info.pop('hostname')
print val

for key in info:
    print key, '-> ' , info[key]
