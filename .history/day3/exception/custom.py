#!/usr/bin/env python

class RangeError(Exception):
    pass

try:
    n = 7
    if n > 5:
	raise RangeError, "%s: value is not in the range" % n

except RangeError, e:
    print "%s: %s" % (e.__class__.__name__, e)
