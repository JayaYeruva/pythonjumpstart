#!/usr/bin/env python

class RangeError(Exception):
    def __str__(self):
	return "<%s: %s>" % (self.__class__.__name__, self.message)

try:
    n = 3
    if not (5<=n<=12):
	raise RangeError, '%s: value not in the range' % n
except RangeError, e:
    print type(e)
    print e
	
