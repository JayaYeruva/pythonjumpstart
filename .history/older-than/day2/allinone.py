#!/usr/bin/env python
import sys

def put_all_in_one(*args):
  with open(args[-1], 'w') as fw:
    for f_name in args[1:-1]:
      with open(f_name) as fp:
        fw.write(f_name.center(60, '-')+"\n")
        for line in fp:
           fw.write(line)
        fw.write('-'.center(60, '-')+"\n")

def usage():
  print "Usage  :"
  print "%s files[ ....] dest" % sys.argv[0]
  exit(1)

if len(sys.argv) < 3:
  usage()

put_all_in_one(*sys.argv)
