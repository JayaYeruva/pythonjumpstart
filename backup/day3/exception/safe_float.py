#!/usr/bin/env python
from sys import argv

def safe_float(value):
   try:
        return  float(value[1])
   except ValueError, e:
	print e
   except (IndexError, KeyError), e:
	print e.__class__
	print e
   except Exception, e:
	print e.__class__
	print e
   finally:
	print 'finally block'

print safe_float(argv)
