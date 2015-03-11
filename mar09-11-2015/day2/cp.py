__author__ = 'ravi'
from sys import argv


def usage():
    print "usage:"
    print "{} source-file dest-file".format(argv[0])
    exit(1)

if len(argv) != 3:
    usage()

print argv
open(argv[2], 'w').write(open(argv[1]).read())
