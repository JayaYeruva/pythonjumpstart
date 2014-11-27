#!/usr/bin/env python

class CSV2JSON(object):
    def __init__(self, data_file, json_file='default.json'):
        self.data_file = data_file
	self.json_file = json_file  
	self.content = None

    def to_xml(self, xmlfile=None):
	with open(xmlfile, 'w') as xml:
	    xml.write('<?xml version="1.0"?>')
	    xml.write('<passwd>')
	    xml_str = ''
	    for record in self.content:
		xml_str += '<user>'
		for title in record:
		    xml_str += "<%s>%s</%s>" %\
				 (title, record[title], title)
		xml_str += '</user>'
	    xml.write(xml_str)
	    xml.write('</passwd>')

    def to_json(self):
	self.__parse_csv()
	self.__to_json()

    def __parse_csv(self):
	with open(self.data_file) as fp:
	    header = fp.readline().rstrip().split(',')
	    self.content = \
	[ dict( zip(header, line.rstrip().split(':'))) \
				for line in fp ]
    def __to_json(self):
	import json
	with open(self.json_file, 'w') as json_fd:
            json.dump(self.content, json_fd)
 
if __name__ == '__main__':
    from sys import argv
    from pprint import pprint	
    doit = CSV2JSON(argv[-2], argv[-1])
    doit.to_json()
    doit.to_xml('passwd.xml')



