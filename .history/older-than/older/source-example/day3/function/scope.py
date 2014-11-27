#!/usr/bin/python
n = 100    #global

def demo():
   global n  #help's us to refer a global vari
   n = 'python'  
   print n

demo()
print n

print __doc__
print __name__
