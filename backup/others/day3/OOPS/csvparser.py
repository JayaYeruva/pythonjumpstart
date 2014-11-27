#!/usr/bin/env python

class CSVParser(object):
    def __init__(self, csvfile):
	self.csvfile = csvfile
	self.content = []
	self.load_content()

    def load_content(self):
	keys = ['latitude', 'longitude', 'description']
	for record in open(self.csvfile).readlines()[1:]:
	    self.content.append( dict( zip( keys, record.rstrip().split(',')) ) )

if __name__ == '__main__':
    from sys import argv	
    from pprint import pprint
    parse = CSVParser(argv.pop())
    pprint(parse.content )
