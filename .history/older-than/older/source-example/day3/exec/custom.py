#!/usr/bin/python

class UserError (Exception):
    def __init__(self, msg):
	self.msg = msg

    def __str__(self):
	return "%s: %s" % (self.__class__.__name__, self.msg) 

try:
    """
    if 1 == 2:
	pass
    else:
        raise UserError, "not the same"
    """
    assert 1==2,   "both are not the same"

except UserError, e:
    print e
