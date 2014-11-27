#!/usr/bin/python
import sys
def safe_float(n):
    value = None
    info = {}	
    try:
          value = float(n)
          #value/0
	  raise NameError, "this is custom exception"
    except ValueError, e:
	print e
    except (ZeroDivisionError, KeyError, IndexError),  e:
	print e
    except Exception, e:
	print "Exception : %s " % e
        print sys.exc_type
    else:
	print "if and only if try block is suc..."
    return value 


print safe_float(3)
print "its all over"
