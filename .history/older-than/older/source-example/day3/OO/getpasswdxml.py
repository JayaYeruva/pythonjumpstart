#!/usr/bin/python
#import getpasswd
#import sys
#sys.path.insert(0, 'lib')
from getpasswd import Passwd
class PasswdXML(Passwd):
     def __init__(self, filename):
	super(PasswdXML, self).__init__(filename) 
	#call's the base constructor
     
     def getPasswdXML(self):
	with open('passwd.xml', 'w') as fw:
            fw.write('<?xml version="1.0" ?>')
            fw.write('<users>')
	    for user in self.passwd:
	        name = user['user'];
		user.pop('user')
	        fw.write('<%s>' % name)
	        u_keys = user.keys()
	        u_keys.sort()
		for k in u_keys:
		    fw.write("<%s>%s</%s>" % (k, user[k], k))
	        fw.write('</%s>' % name)
            fw.write('</users>')

p = PasswdXML('/etc/passwd')
p.getPasswdXML();
