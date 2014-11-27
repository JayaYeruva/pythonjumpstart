# IPython log file

get_ipython().magic(u'quickref')
get_ipython().magic(u'logstart ')
get_ipython().system(u'ls -F --color ')
date 
get_ipython().magic(u'date')
get_ipython().system(u'date')
get_ipython().system(u'cd /etc')
import os
os.getcwd()
get_ipython().system(u'pwd')
get_ipython().system(u'cd /etc')
get_ipython().system(u'echo $?')
d = {}
type(d)
d = {'name':'peter'}
d = {'name':'peter', 'age':33, 'gender':'male'}
d = {'name':'peter', 'age':33, 'gender':'male'}
len(d)
d
d = {'name':'peter', 'age':33, 'gender':'male'}
d
d['city'] = 'bangalore'
d
d['county'] = 'karnataka'
d
d.remove('county')
dir(d)
d
d.pop('county')
d
d['ccity'] = 'chennai'
d
del(d['ccity'])
d
k = 'city'
d
d.has_key(k)
if d.has_key(k):
     d[k] = 'chennai'
    
d
d['zero']
d
d.keys()
d.values()
d.items()
l = d.items()
l
dict( l )
list(d)
d
for key in d.keys():
     print "%s : %s" % (key, d[key])
    
for (k, v) in d.items():
     print "%s : %s" % (k, v)
    
passwd = {'root' : {'login':'root'. 'password':'x', 'uid':0, gid:0}}
passwd = {'root' : {'login':'root', 'password':'x', 'uid':0, gid:0}}
passwd = {'root' : {'login':'root', 'password':'x', 'uid':0, 'gid':0}}
d.values()
d.keys()
for k in d.keys():
    print k, "->", d[k]
    
d.items()
for (k, v) in d.items();
for (k, v) in d.items():
    print k, ':', v
    
d.items()
passwd = {'root' : {'login':'root', 'password':'x', 'uid':0, 'gid':0}}
passwd['root']
passwd['root']['gid']
passwd['root']['login']
passwd
passwd = {'root': {'gid': 0, 'login': 'root', 'password': 'x', 'uid': 0}, 
 'mysql': {'gid': 100, 'login': 'mysql', 'password': 'x', 'uid': 100},  
}
passwd = {'root': {'gid': 0, 'login': 'root', 'password': 'x', 'uid': 0}, 
 'mysql': {'gid': 100, 'login': 'mysql', 'password': 'x', 'uid': 100},  
}
passwd 
for ch in 'python':
    print ch
    
3 in range(1,5)
get_ipython().magic(u'pprint ')
import pprint
pprint.pprint
pprint.pprint([])
l = [3, 2, 1, 5, 3, 8, 1, 2, 9,  1, 4, 2, 7, 6,3]
l
set(l)
type( set(l) )
set(l)
a = set(l)
a
b = set([1,2,3])
c = set([4,5,6])
d = set([7,8,9])
b.intersect(c)
a
b
c
dir(a)
b.intersection(c)
b.intersection(a)
b.add(9)
b
c
d
b.intersection(d)
a.issuperset(b)
b
a
a - b
a
b
dir(a)
b.remove(9)
b
c
c.clear()
c
a
100 in a
dir(b)
b
c
d
d 
b
d + b 
d
d.add(100)
d
d
list(d)
tuple(d)
d
import re
s = 'perl and python'
help(re.match)
re.match(r'perl', s) 
re.match(r'python', s)
re.match(r'Perl', s)
re.match(r'Perl', s, re.I)
re.search(r'python', s)
m = re.search(r'python', s)
m.start()
m.end()
s
m.span()
m.group()
m = re.search(r'python', s, re.I)
dir(File)
dir(file)
fp = open('/etc/passwd')
fp
enumerate(fp)
e = enumerate(fp)
e.next()
del(fp)
s
s = 'a sample string for the python sub'
help(re.sub)
re.sub('a', 'A', s)
re.sub('a', 'A', s, count=1)
re.sub('A', 'A', s, count=1 )
s
re.sub('A', 'A', s, count=1 , re.I)
re.sub('A', 'A', s, 0 , re.I)
re.sub('A', 'A', s, 1 , re.I)
re.sub('A', 'A', s,  , re.I)
re.sub('A', 'A', s, 0 , re.I)
re.sub('A', 'A', s, flag=re.I)
re.sub('A', 'A', s, flags=re.I)
re.sub('A', 'A', s, flags=re.I)
s
re.sub('a', 'A', s, count=1)
re.sub('a', 'A', s)
re.sub('a', 'A', s, count=2, flags=re.I)
s
import string
help(str.translate)
tab = string.maketrans('aeiou', AEIOU)
import string
tab = string.maketrans('aeiou', 'AEIOU')
s
s.translate(tab)
tab = string.maketrans('aeiou', '^3!@V)
tab = string.maketrans('aeiou', '^3!@V')
s.translate(tab)
s
tab
l
map (str, l)
str
l
sum(l)
t = (10, )
t
t = (10)
s = ('peter')
t
s
s = ('peter', )
s
len(s)
l = ['f1', 'f2', 'f3', 'dest']
l = ['f1', 'f2', 'f3', 'myfile']
dest = l[-1]
dest = l.pop()
l
dest = l[-1]
dest
l
l[:-2]
l = ['f1', 'f2', 'f3', 'myfile']
l[-1]
l[:-1]
file
dir(file)
dir(fp)
dir(file)
'passwd'.center(50, '-')
'passwd'.center(50, '-')
dir(str)
dir()
import utils
help(super)
l = [['peter', 'tim', 'kimberly'], ['la', 'ma', 'ca']]
b_l = l 
del(l[1])
b_l
#shallow copy 
id(l)
id(b_l)
l
b = l
import copy
dl = copy.deep_copy(l)
dl = copy.deepcopy(l)
l
import copy
dl = copy.deepcopy(l)
id(l)
id(dl)
dl
l
l.append('peter')
l
dl
import filecmp
help(filecmp.cmp)
import shutils
import shutil
dir(shutil)
help(shutil)
shutils.copystat('/etc/passwd', 'passwd')
shutil.copystat('/etc/passwd', 'passwd')
