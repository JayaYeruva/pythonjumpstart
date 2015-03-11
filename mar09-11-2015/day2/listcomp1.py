__author__ = 'ravi'


mat = [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]
"""
print [r[1] for r in mat]
"""

print [c for r in mat for c in r if c % 2 and len(r) == 3]