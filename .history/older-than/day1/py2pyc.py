#!/usr/bin/env python

import compiler
import sys

def usage():
    print "Usage :"
    print sys.argv[0], "python_script"
    exit(1)

if len(sys.argv) != 2:
    usage()

compiler.compileFile( sys.argv[1] )
