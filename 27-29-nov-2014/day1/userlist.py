__author__ = 'ravi'

datafile = '/etc/passwd'
userlist = []

with open(datafile) as fp:
    for l in fp:
        userlist.append(l.split(':')[0].upper())

l = 1
with open('userlist.dat', 'w') as fw:
    for name in sorted(userlist):
        content =  "{:>6}  {}".format(l, name)
        print content
        fw.write(content+'\n')
        l += 1

#from pprint import pprint
#pprint(userlist)

