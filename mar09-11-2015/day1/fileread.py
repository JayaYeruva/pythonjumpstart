__author__ = 'ravi'
"""
with is context manager scope
"""

with open('/etc/passwd') as fp:
   for line in fp:
       if line.startswith('#'):
           continue   #transfer control to the ln no. 7
       print line.rstrip("\n")