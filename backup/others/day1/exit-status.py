#!/usr/bin/env python
from random import randint
from sys import stderr
import sys
value = randint(1, 1000)
print "%s value in the range" % value

if value>500:
   print  >>stderr, 'exit-status: %s: value not in the range' % (value)
   sys.exit(1)
elif 200 <= value <= 500:
   pass  #pass statement  gives dummy code block
elif 100 <= value < 200:
   pass
   

