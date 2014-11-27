#!/usr/bin/python
import sys

def safe_float(val):
    try:
        val = float(val)
        raise IndexError, "unknown index"
        d = {}; d['peter'];
        res = val/0
    except (ValueError, KeyError), e:
        val = None
        print e
        print sys.exc_type
        exit(1)
    except ZeroDivisionError, e:
        val = None
        print e
        exit(2)
    except Exception, e:
	print "IndexError ", e
        exit(2)
	
    return val    

print safe_float(sys.argv[1])
