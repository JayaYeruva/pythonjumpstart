#!/usr/bin/env python
# encoding: utf-8
#

#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import subprocess

print 'popen2:'

proc = subprocess.Popen(['cat', '-'],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
print proc
msg = 'through stdin to stdout'
stdout_value = proc.communicate(msg)[0]
print '\tpass through:', repr(stdout_value)
