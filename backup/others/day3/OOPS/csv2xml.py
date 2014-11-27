#!/usr/bin/env python
from csvparser import CSVParser

class CSV2JSON(CSVParser):
    def __init__(self, csvfile, jsonfile):
	self.jsonfile = jsonfile
	super(CSV2JSON, self).__init__(csvfile)
	self.writeJSON()

    def writeJSON(self):
	import json
	fw = open(self.jsonfile, 'w')
	json.dump(self.content, fw)
	fw.close()

class CSV2XML(CSVParser):
    def __init__(self, csvfile, xmlfile):
	self.xmlfile = xmlfile
	super(CSV2XML, self).__init__(csvfile)
	self.writeXML()

    def writeXML(self):
	xml = open(self.xmlfile, 'w')
	xml.write('<?xml version="1.0" ?>')
        xml.write('<gps-data>')
	for location in self.content:
	   temp =  '<location latitude="%s" longitude="%s">' % \
			(location['latitude'], location['longitude'])
	   temp += '<description>%s</description>' % location['description']
	   temp += '</location>'
	   xml.write(temp)
        xml.write('</gps-data>')
	xml.close()

if __name__ == '__main__':
    from sys import argv	
    from pprint import pprint

    if argv[-1].endswith('xml'):	
	parse = CSV2XML(argv[-2], argv[-1])
    elif argv[-1].endswith('json'):	
	parse = CSV2JSON(argv[-2], argv[-1])
    	
