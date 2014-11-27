#!/usr/bin/env python

class Passwd(object):
    def __init__(self, filename):
	self.filename = filename
        self.passwd = []
        with open(self.filename) as fp:
	    for line in fp:
		user = line.rstrip().split(':')
	        self.passwd.append(   \
		 { 'user' : user[0], 'passwd': user[1], \
		   'uid' : user[2], 'gid': user[3], \
		   'gecos' : user[4], 'dir':user[5],\
		   'shell' : user[6]} )

    def getPasswd(self):
        for user in self.passwd:
	    user_keys = user.keys()
	    user_keys.sort()
            for k in user_keys:
		print "%20s : %s" % (k, user[k])
	    print 
if __name__ == '__main__':
    p = Passwd('/etc/passwd')
    p.getPasswd()

