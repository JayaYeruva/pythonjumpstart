__author__ = 'ravi'

info = dict(name='python', version='2.7', author='rossum')
"""
updating an element of the dict
"""
if 'version' in info:
    info['version'] = '3.3'

"""
add a new element to the dict
"""
info['release'] = 'spherical cow'

print info.values()
print info.keys()
print info.items()
"""
for k in sorted(info):
    print "{} : {}".format(k, info[k])
"""
