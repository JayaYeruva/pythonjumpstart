#!/usr/bin/python

class UserError (Exception):
    def __init__(self, msg):
	self.mesg = msg

    def __str__(self):
	return "%s : %s" % (self.__class__.__name__, self.mesg)


try:
    n = input('Enter the number : ')
    #if n < 100:
    #    raise UserError, "value is too low to consider"
    assert  n > 100,  "value is too big"
except UserError, e:
	print e
