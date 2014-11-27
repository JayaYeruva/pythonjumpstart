#!/usr/bin/env python
import re

#match
s = 'the python scripting and the python'

print re.match('pYthon', s, re.I)

