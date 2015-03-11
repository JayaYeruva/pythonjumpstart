__author__ = 'ravi'
#from module import item1,....
from pprint import pprint

names = ["sax", 'pax', "steve", 'json']
version = [0.1, 0.3, 1.4, 2.2]
platform = ['py', 'py', 'unknown', 'js']

"""
parallel iteration
"""

for n, v, p in zip(names, version, platform):
    print "{:>22} {:>6} {:>10}".format(n, v, p)

