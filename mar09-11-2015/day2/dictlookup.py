__author__ = 'ravi'

info = dict(name='python', version='2.7', author='rossum')

print info['name']
print info['version']
print info.get('author')
print info.get('authorr')
print info.get('authorr', 'intuit')

