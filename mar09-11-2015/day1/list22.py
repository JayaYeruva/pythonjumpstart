__author__ = 'ravi'
#from mod import item
from random import shuffle
l = range(1, 11)
shuffle(l)

print filter(lambda val: val % 2 == 0, l)

"""
print map(lambda value: value ** value, l)


print l
print sum(l)

print map(hex, l)
"""