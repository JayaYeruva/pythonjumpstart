#!/usr/bin/env python


import subprocess
import sys

proc = subprocess.Popen(['python', 'pycat.py'],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
stdout_value = proc.communicate(raw_input('Enter the content: '))[0]
print '\tpass through:', repr(stdout_value)
