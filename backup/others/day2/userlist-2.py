#!/usr/bin/env python
from pprint import pprint

res = [ line.rstrip().split(':')[0].title() \
     for line in open('/etc/passwd') if line.startswith('a') or line.startswith('h')]

pprint(res)
