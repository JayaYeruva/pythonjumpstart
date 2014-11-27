#!/usr/bin/env python

def demo(*args):
    print args


demo()
#demo('python')
#demo(1)
#demo(1,2,3,4)
#demo('a', 'e', 'i', 'o', 'u')

l = [1,3,5,7,13]
t = (2,4,6,8)

demo(l)
demo(*l)
demo(t)
demo(*t)

