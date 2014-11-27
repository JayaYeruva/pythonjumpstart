#!/usr/bin/env python

import sys
userlist = []
tags = ['name', 'password', 'uid', 'gid', 'gecos', 'directory', 'shell']

def toxml(userlist, f_name):
  with open(f_name, 'w') as fw:
    fw.write('<?xml version="1.0" ?>')    
    fw.write('<passwd>')    
    for user in userlist:
      fw.write('<user>')    
      for tag in tags:
        fw.write("<%s>%s</%s>" % (tag,  user[tag], tag))	  
      fw.write('</user>')    
    fw.write('</passwd>')    

def loadrecords(filename):
  with open(filename) as fp:
    for line in fp:
      line = line.rstrip()
      temp = line.split(':')
      userinfo = {
	  tags[0] : temp[0],	
	  tags[1] : temp[1],	
	  tags[2] : temp[2],	
	  tags[3] : temp[3],	
	  tags[4] : temp[4],	
	  tags[5] : temp[5],	
	  tags[6] : temp[6],	
        }
      userlist.append(userinfo)

loadrecords(sys.argv[1])
#import pprint
#pprint.pprint(userlist)
toxml(userlist, 'passwd.xml')

