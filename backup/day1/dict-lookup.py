#!/usr/bin/env python

info = {'hostname':'ws1.rootcap.in', 'ipaddr':'132.12.12.1', 
	 'purpose':'workstation', 'platform' : 'linuz2'
	}

print info['hostname']
print info['ipaddr']
print info['purpose']
print info.get('platformm')
print info.get('platformm', 'unknown key')

