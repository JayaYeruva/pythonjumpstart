#!/usr/bin/env python

from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = parse('movies.xml')
collection = DOMTree.documentElement

if collection.hasAttribute('shelf'):
    print "Root element : %s" % collection.getAttribute("shelf")
