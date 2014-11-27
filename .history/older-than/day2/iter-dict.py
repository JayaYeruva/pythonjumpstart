#!/usr/bin/env python

passwd = {
	'root': 	
	'mysql': {'gid': 100, 'login': 
		'mysql', 'password': 'x', 'uid': 100},  
}

for user in passwd.keys():
    for key in passwd[user].keys():
	print "%s : %s" % (key, passwd[user][key])
    print 
