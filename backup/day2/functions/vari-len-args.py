#!/usr/bin/env python

def demo(*args):
    print args

demo()
demo(10)
demo('pypi')
demo(12.12)

t = ('a', 'e', 'i', 'o', 'u')
l = [1,2,3,4]
demo(l)
demo(t)
demo(1,2,3,4)
demo(1, 'one', 1.0)

