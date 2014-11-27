#!/usr/bin/env python

import sys

def safe_float(value, value2):
  try:
      return ( float(value) / float(value2) ) * sys.argv[3]
  except ValueError, e:
      print e
      return 0.0
  except ZeroDivisionError, e:
      print e
      return 0.0
  except (IndexError, KeyError), e:
      print e
      return 0.0
  except Exception, e:
      print e
      return 0.0
  finally:
      print "finally block....."

print safe_float(sys.argv[1], sys.argv[2])
