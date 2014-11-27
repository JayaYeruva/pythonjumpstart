#!/usr/bin/env python
from sys import argv
from pprint import pprint

f_name = ''
lookup = {}

def usage():
    print "Usage:"
    print "%s database-name search-key" % argv[0]
    exit(1)

if len(argv) != 3:
    usage()

if argv[1] == 'passwd':
    f_name = '/etc/passwd'
else:
    print "%s: %s: invalid or unknown database name" % \
	(argv[0], argv[1])
    exit(2) 

with open(f_name) as fp:
    for line in fp:
        (login, passwd, uid, gid, gecos, home, shell) = \
	      line.rstrip().split(':')
        lookup[login] = {}
        lookup[login]['passwd'] = passwd
        lookup[login]['uid'] = uid
        lookup[login]['gid'] = uid
        lookup[login]['gecos'] = gecos
        lookup[login]['home'] = home
        lookup[login]['shell'] = shell

if lookup.has_key(argv[2]):
    print "login :", argv[2]
    for key in lookup[argv[2]]:
	print "%s : %s" % (key, lookup[argv[2]][key])
else:
    print "%s: %s: invlaid key" % (argv[0], argv[2])
    exit(3)
#pprint(lookup)

