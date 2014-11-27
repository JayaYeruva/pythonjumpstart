#!/usr/bin/env python

from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = parse('movies.xml')
collection = DOMTree.documentElement

if collection.hasAttribute('shelf'):
    print "Root element : %s" % collection.getAttribute("shelf")

movies = collection.getElementsByTagName('movie')

for movie in movies:
    if movie.hasAttribute('title'):
        title = movie.getAttribute('title')
	print "Title : %s" % title
