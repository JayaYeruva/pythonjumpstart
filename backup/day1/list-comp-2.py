#!/usr/bin/env python

l = [1,2,3,4,5]
bi = [ bin(item) for item in l ]
print bi

dec = [ int(binary, 2) for binary in bi]
print dec 
