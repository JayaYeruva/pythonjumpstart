#!/usr/bin/env python

info = {'hostname':'ws1.rootcap.in', 'ipaddr':'132.12.12.1', 
	 'purpose':'workstation', 'platform' : 'linuz2'
	}

if info.has_key('purpose'): 
    info['purpose'] = 'lab server'

for key in info:
    print key, '-> ' , info[key]
