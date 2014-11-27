#!/usr/bin/env python
from sys import argv
def center(s, w, f=''):
    mid = (w - len(s))/2
    return "%s%s%s" % (f*mid, s, f*mid)


print center(argv[1], int(argv[2]), argv[3])
