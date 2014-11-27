#!/usr/bin/env python

from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = parse('movies.xml')
collection = DOMTree.documentElement

if collection.hasAttribute('shelf'):
    print "Collection : %s" % collection.getAttribute("shelf")

movies = collection.getElementsByTagName('movie')

for movie in movies:
    print 'Movie'.center(30,'-')
    if movie.hasAttribute('title'):
        title = movie.getAttribute('title')
	print "Title : %s" % title

    typ = movie.getElementsByTagName('type')[0]
    print "Type : {} ".format(typ.childNodes[0].data) 

    fmt = movie.getElementsByTagName('type')[0]
    print "Type : {} ".format(typ.childNodes[0].data) 

    rating = movie.getElementsByTagName('rating')[0]
    print "Rating : {} ".format(rating.childNodes[0].data) 
    
    stars = movie.getElementsByTagName('stars')[0]
    print "Stars : {} ".format(stars.childNodes[0].data) 
    
    desc = movie.getElementsByTagName('description')[0]
    print "Description : {} ".format(desc.childNodes[0].data) 
    print 
