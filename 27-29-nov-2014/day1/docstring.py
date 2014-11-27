__author__ = 'ravi'

n = 'x'

s = '''
    1
   2 2
  3 {} 3
   4 4
    5
'''.format(n)

print s.strip('\n')
