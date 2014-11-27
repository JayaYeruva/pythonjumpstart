from fileinput import input, lineno

for line in input():
    print "%6s  %s" % (lineno(), line), 
