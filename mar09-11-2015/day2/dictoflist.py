__author__ = 'ravi'
from pprint import pprint as pp
"""
info = {l.split(':')[0]: l.rstrip().split(':')[1:]
        for l in open('/etc/passwd')}
"""
info = dict()

for l in open('/etc/passwd'):
    temp = l.rstrip().split(':')
    info[temp[0]] = temp[1:]

for login in info:
    print "{}:{}".format(login, info[login][-1])