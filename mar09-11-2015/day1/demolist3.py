__author__ = 'ravi'

l = [1, 1.0, 'one', 3+4j]
l[1] = 'bangalore'

temp = l[-2]
l[-2] = l[-1]
l[-1] = temp

print l

