__author__ = 'ravi'


info = dict([('release', 'spherical cow'), ('version', '3.3'),
 ('name', 'python'), ('author', 'rossum')])

print info.keys()

for k in info:
    print k, '->', info[k]
