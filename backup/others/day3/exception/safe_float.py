#!/usr/bin/env python 
from sys import argv
import sys
def safe_float(data):
     	
    try:
        result = 0.0
        result = float(data[1])
    except ValueError, e:
        print e
#    except (KeyError, IndexError), e:
#	print 'index/key ', e
    except Exception, e:
        tb = sys.exc_info()[-1]
 	import traceback
	traceback.print_tb(tb)

	print 'internal server error'
    finally:
	return result
 
print safe_float(argv)
print 'reached here'

