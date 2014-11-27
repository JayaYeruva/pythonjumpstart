#!/usr/bin/env python

class RangeError(Exception):
    def __init__(self, message):
	self.message = message.upper()

    def __str__(self):
	return "%s: %s" % (self.__class__.__name__, self.message)

n = 15

try:
    if not 1<=n<=10:
        raise RangeError, '%s: value not in the range' % n
except RangeError, e:
    print e
