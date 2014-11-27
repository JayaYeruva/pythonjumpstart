#!/usr/bin/env python
import pprint
import sys

def get_db(key):
  db = { 
	'passwd' : '/etc/passwd', 
	'group'  : '/etc/group',
   	}
  if db.has_key(key):
    return db[key]  
  else:
    print "%s: %s: invalid database" % (sys.argv[0], sys.argv[1])
    exit(2) 

def usage():
  print "Usage:"
  print "%s database key " % sys.argv[0]
  exit(1)

if len(sys.argv) != 3:
  usage() 

lookup = {}

with open(get_db(sys.argv[1])) as fp:
  for line in fp:
     line = line.rstrip()
     temp = line.split(':')
     lookup[ (temp[0], temp[2]) ] = line     

for key in lookup.keys():
  if sys.argv[2] in key:
      print lookup[key]
      exit(0)

print "%s: %s: invalid key" % (sys.argv[0], sys.argv[2])
exit(3) 

