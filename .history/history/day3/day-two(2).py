# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# dict, for the purpose of the lookup db

# <codecell>

info = {'name':'rosvas', 'age':4, 'gender' : 'male'} 
print len(info)

# <codecell>

info = {'name':'rosvas', 'age':4, 'gender' : 'male', 'city':'bangalore'} 
print info

# <codecell>

info = {'name':'rosvas', 'age':4, 'gender' : 'male', 'city':'bangalore'} 
info['citty'] = 'jersy'
print info

# <codecell>

info = {'name':'rosvas', 'age':4, 'gender' : 'male', 'city':'bangalore'} 
info['interest'] = 'read'
print info.has_key('city')
if info.has_key('city'):
    info['city'] = 'jersy'
del(info['city'])
print info

# <codecell>

info = {'name':'rosvas', 'age':4, 'gender' : 'male', 'city':'bangalore'} 
print info.values()
print info.keys()
print info.items()

# <codecell>

info = {'name':'rosvas', 'age':4, 'gender' : 'male', 'city':'bangalore'} 
for key in info:
    print "%s -> %s" % (key, info[key])

# <codecell>

info = {'name':'rosvas', 'age':4, 'gender' : 'male', 'city':'bangalore'} 
keys = info.keys()
keys.sort()
for k in keys:
    print "%s : %s" % (k, info[k])

# <codecell>

info = {'name':'rosvas', 'age':4, 'gender' : 'male', 'city':'bangalore'} 
print info.items()
for (k, v) in info.items():
    print k, ' : ', v

# <codecell>

person = {}
person['f_name'] = 'paul'
person['l_name'] = 'allen'
person['age'] = '4'
person['founder'] = 'ms'
print person

# <codecell>

s = 'root:x:0:0:root:/root:/bin/bash'
l = s.split(':')
print l
(login, passwd, uid, gid, gecos, home, shell) = s.rstrip().split(':')  #tuple assginment
print login
print passwd
print uid
print gid
print gecos
print home 
print shell

# <headingcell level=1>

# tuple

# <codecell>

t = (1,2,3,4,5)
print len(t)

# <codecell>

t = (1,2,3,4,5)
t = 'james', 'lee'
print t

# <headingcell level=1>

# tuple assginment

# <codecell>

name, age, gender = 'ram', 3, 'male'
print name
print age
print gender

# <codecell>

(a, b) = (10, 20)
(a, b) = (b, a)
print a, b

# <codecell>

info = {'name':'rosvas', 'age':4, 'gender' : 'male', 'city':'bangalore'} 

for k, v in info.items():
    #k, v = t
    print k, ':', v

# <codecell>

t = 'peter', 'perl', 'eng-us'
l = list(t)
l[1] = 'pear'
t = tuple(l)
print t

# <codecell>

t = ('peter pan',)
print t

# <codecell>

t = 'peter', 'perl', 'eng-us', 'perl'
print t.index('perl',2)
print t.count('perl')

# <codecell>

t = 'peter', 'perl', 'eng-us', 'perl'
print t * 3

# <codecell>

import re
s = 'the Perl scripting'
print re.match(r'perl', s, re.I)  #raw string

# <codecell>

import re
s = 'the Perl scripting'
m = re.search(r'perl', s, re.I)  #raw string
if m:
    print "matched :",  m.group()
    print "start index :", m.start()
    print "end index :", m.end()
    print m.span()

# <codecell>

import re
s = 'the perl scripring and the perl scripring'
print re.sub(r'perl', 'python', s, flags=re.I)

# <codecell>

s = 'root,password;100-100!admin,/root;/bin/bash'
import re
print re.split(r'[,;\-,!]', s)

# <headingcell level=1>

# functions

# <codecell>

def demo():
    return 'a sample function'

print demo()

# <codecell>

def dummy():
    pass

    

# <codecell>

def power(x, n):
    return x ** n

print power(2, 3)

# <codecell>

print sum([])
print sum([1,2,3])
print sum((4,5,6,7))

# <codecell>

def 

