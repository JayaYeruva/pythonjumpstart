#!/usr/bin/env python
import sys 
import pprint
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
        row = line.split(':')
	lookup[(row[0], row[2])] = line.rstrip()

lookup_key = None

id_keys = lookup.keys()
for key_t in  id_keys:
    if sys.argv[2] in key_t:
        lookup_key = key_t
        break

if lookup_key == None:
    print "%s : %s : invalid key" % (sys.argv[0], sys.argv[2])
    exit(2) 
 
print lookup[lookup_key]



