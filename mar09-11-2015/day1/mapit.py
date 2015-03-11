__author__ = 'ravi'

s = 'perl'

"""
res = map(ord, s)
res = map(lambda char: char.upper(), s)
"""
res = map(lambda item: "<char>{}</char>".format(item), s)
print res

