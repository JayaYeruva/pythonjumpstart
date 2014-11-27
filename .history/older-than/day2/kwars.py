#!/usr/bin/env python

def demo(**kwargs):
   print kwargs

info = { 'version':'linux2', 'arch':'x68_64', 'release':'beefycow'}
demo()
demo(name='nelson', lang='us-gn', gender='male')
demo(**info)
