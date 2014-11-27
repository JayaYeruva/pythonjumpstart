#!/usr/bin/env python

info = {'name' : 'guido', 'lang' : 'python', 'city':'san jose', 'area': 'lakeview'}

info['mobile'] = '9790912345'
info['email'] = 'guido@psf.com'

print info.keys()
print info.values()
print info.items()
print;print
for k in info:
   print "%s -> %s" % (k, info.get(k))
