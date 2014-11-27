#!/usr/bin/env python

info = {'name' : 'guido', 'lang' : 'python', 'city':'san jose', 'area': 'lakeview'}

info['mobile'] = '9790912345'
info['email'] = 'guido@psf.com'

print info.get('name')
print info.get('lang')
print info.get('cityy')
print info.get('cityy', 'unknown key')
