#!/usr/bin/env python

import sys

def headntail(filename, **options):
   count = 10
   
   if options.has_key('count'):
      count = options['count']
   
   if options.has_key('order'):
      if options['order'] == 'tail':
         return ''.join(open(filename).readlines()[-(count):])
      elif options['order'] == 'head':
         return ''.join(open(filename).readlines()[:count])
   else:   
      return ''.join(open(filename).readlines()[:count])

print headntail(sys.argv[1], count=5, order='tail'), 
