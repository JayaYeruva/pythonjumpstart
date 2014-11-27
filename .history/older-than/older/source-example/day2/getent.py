#!/usr/bin/env python
import sys 

def usage(): #function definition
    print "Usage:"
    print "%s dbname lookup-key" % sys.argv[0]
    exit(1)

if len(sys.argv) != 3:
    usage() #function calling

f_name = None
lookup = {}

if sys.argv[1] == 'passwd':
    f_name = '/etc/passwd'
elif sys.argv[1] == 'group':
    f_name = '/etc/group'
else:
    print "%s : %s : invalid db" % (sys.argv[0], sys.argv[1])
    exit(3)
    
with open(f_name, 'r') as fp:
    for line in fp:
	lookup[ line.split(':')[0] ] = line.rstrip()

if lookup.has_key(sys.argv[2]):
    print lookup[sys.argv[2]]
else:
    print "%s : %s : invalid key" % (sys.argv[0], sys.argv[2])
    exit(2) 




