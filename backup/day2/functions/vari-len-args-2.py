#!/usr/bin/env python

def demo(*args):
    print args

t = ('a', 'e', 'i', 'o', 'u')
l = [1,2,3,4]
demo(l)
demo(*l)  #content list is passwd as arguments

demo(t)
demo(*t) 

