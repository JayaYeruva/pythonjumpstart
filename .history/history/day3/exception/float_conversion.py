#!/usr/bin/env python
import sys

def safe_float(value):
    val = 0.0
    try:
         print name
         val = float(value[1])
    except ValueError, e :
	print e 
    except (IndexError, KeyError), e:
        print e
    except ZeroDivisionError, e:
	print e
    except Exception,  e:
	print e
        print sys.exc_type
    else:
	print 'else block will execute, if & only if try wo any exe'
    return val


import sys
print safe_float(sys.argv)

