__author__ = 'ravi'
import re

s = 'the python and the perl scripting'
c = re.compile('PythoN', re.I)

m = c.search(s)

if m:
    print "matched : {}".format(m.group())
    print m.start()
    print s[m.end():]
    print m.span()
else:
    print "fails to match"
