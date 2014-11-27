#!/usr/bin/env python

import sys 

class RangeError(Exception):
  def __init__(self, mesg):
	self.mesg = mesg

  def __str__(self):
	return "%s: %s" % ( self.__class__.__name__, self.mesg)

value = float(sys.argv[1])
try:
    if not (3<=value<=8):
       raise RangeError,  'value not in the range'
except RangeError, e:
    print e
 
