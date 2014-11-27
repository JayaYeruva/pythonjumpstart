#!/usr/bin/env python
from pprint import pprint
import json

keys = ['login', 'passwd', 'uid', 'gid', 'gecos', 'home', 'shell']

content = [ dict(zip(keys, line.rstrip().split(':'))) \
			for line in open('/etc/passwd')]

js =  json.dumps(content)

struct = json.loads(js)  #json into python type
print struct[0]
