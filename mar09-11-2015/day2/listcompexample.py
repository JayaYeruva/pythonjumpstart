__author__ = 'ravi'
from pprint import pprint as pp


ul = sorted([l.split(':')[0].title() for l in open('/etc/passwd')
                if not l.startswith('#') and l.startswith('a')])

pp(ul)