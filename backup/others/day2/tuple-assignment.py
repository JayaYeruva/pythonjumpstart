#!/usr/bin/env python

hostname, ipaddr, os, release =  'ws1', '3.3.3.6', '2.6.4', 'beffycow'
'''
print hostname
print ipaddr
print os
print release '''

s = 'uucp:x:10:14:uucp:/var/spool/uucp:/sbin/nologin'

login, passwd, uid, gid, gecos, home_dir, shell = s.split(':')

print login
print passwd
print home_dir
print shell
