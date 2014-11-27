#!/usr/bin/env python

info = {'name' : 'guido', 'lang' : 'python', 'city':'san jose', 'area': 'lakeview'}

info['mobile'] = '9790912345'
info['email'] = 'guido@psf.com'

del info['lang']

val = info.pop('name')
print val; print 

if info.has_key('cityy'):
    info['cityy'] = 'sanfrans';

'''
print info['name']
print info['lang']
print info['city']
'''
print info
