#!/usr/bin/env python
#
# Copyright 2010 Doug Hellmann.
#
"""Checking exit codes from external processes
"""
#end_pymotw_header

import subprocess

try:
   res =   subprocess.check_call(['ls', 'peterpan'])
   print res
except subprocess.CalledProcessError as err:
    print 'ERROR:', err
