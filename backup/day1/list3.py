#!/usr/bin/env python

l = [1, 'one', 1.0]
l.append('pypi')
l.append('cpan')

print l; print

value = l.pop(-2)
print value
print l
