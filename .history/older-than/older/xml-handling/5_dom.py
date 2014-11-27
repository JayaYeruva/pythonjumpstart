#!/usr/bin/env python

from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = parse('movies.xml')
collection = DOMTree.documentElement

if collection.hasAttribute('shelf'):
    print "Collection : %s" % collection.getAttribute("shelf")

movies = collection.getElementsByTagName('movie')

for movie in movies:
    print 'Movie'.center(30, '-')
    if movie.hasAttribute('title'):
        title = movie.getAttribute('title')
	print "Title : %s" % title
    for movinfo in  movie.childNodes:
	print "%s : %s" % (movinfo.tagName.title(), movinfo.childNodes[0].data)
    print 
