#!/usr/bin/env python
import sys

def power(x, n=2):
    return x ** n


print power(5)  #calling
print power(5, 3)  #calling
if len(sys.argv) == 3: print power(sys.argv[1], sys.argv[2])  #calling
