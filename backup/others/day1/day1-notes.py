# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import math
dir(math)
math.pi

# <codecell>

#from module import item
from math import pi
pi

# <codecell>

print 1,2,3,4,5

# <codecell>

name = 'python'
version = '2.7.3'

#print 'I am %s' % name
#print 'I am %s and %s' % name, % version) #syntax error
#print 'I am %s and %s' % (name, version)

name = 'pat'
age = 3
gender = 'male'

s = "%s is a %s and %d years old" % (name, gender, age)
#print s


#print "%s|%s|%s|" % (name, gender, age)
print "%10s|%10s|%10.2f|" % (name, gender, age)
print "%10s|%10s|%10.2f|" % (name, gender, age)
print "%10s|%10s|%10.2f|" % (name, gender, age)
print "%-10s%-10s%10s" % (name+'|', gender+'|', str(age)+'|')

# <codecell>

'peter' + 'pan'
'peter' * 3

# <codecell>

n = 2 ** 63
print n
type(n)
n = 15
print n
print hex(n)
print bin(n)
print oct(n)
print int('f', 16)
print int('1111', 2)
print int('17', 8)

# <codecell>

print 0.003
print 3e-3

# <codecell>

n = 4+3j
print n.real
print n.imag
print n.conjugate()
print type(n + n)
print n  * n

# <codecell>

print 5.8/2
print 5.8//2  #floor division

# <codecell>

not (1 != 2)

# <codecell>

# 6 ^ 2
#  110
#^ 010
#  100
print 6  ^ 2

# <codecell>

#right shift 
# 4 >> 1
# 100 >> 1 =  10
# 
# 4 << 1
# 100 << 1 = 1000
print 4 << 1

# <codecell>

#cmp
cmp('bata', 'beta')

# <codecell>

s = 'the python scripting'
#membership test operator  (in), (not in)
print 'zee' not in s

# <codecell>

n = 5
#  ? : 
# true-block if test-condition else false-block
res  = n ** 2 if n>5 else n ** 3
print res

# <codecell>

a, b, c = 12, 4,10   #parallel or tuple assignment 

res = a if (a > b) and (a > c) else b if (b>a) and (b > c) else c
print res

# <codecell>

s = 'python'
#s[2] = 'T'
print id(s)

