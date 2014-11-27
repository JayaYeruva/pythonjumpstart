#!/usr/bin/env python

def demo(**args):
   print args

demo()

demo(name='guido', lang='python', release='green-parrot')

info = {'lang': 'python', 'release': 'green-parrot', 'name': 'guido'}

demo(**info)
