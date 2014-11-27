#!/usr/bin/env python

class RangeError(Exception):
    pass


try:
    n = 6
    if n>5:
        raise RangeError, '%s: value not in the range' % n
except RangeError, e:
    print e

print 'a demo for the custom exception'
