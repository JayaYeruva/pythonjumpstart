__author__ = 'ravi'
from pprint import pprint

content = [line.rstrip().split(':') for line in open('/etc/passwd')
           if not line.startswith('#')]

for user in content:
    print "{}:{}".format(user[0], user[-1])
