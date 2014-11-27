#!/usr/bin/env python
def runme(cmd):
     import subprocess
     ls = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0]
     return ls

if __name__ == '__main__':
   print runme('fortune')
