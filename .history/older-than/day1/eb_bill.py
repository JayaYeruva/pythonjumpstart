#!/usr/bin/env python
import sys
units = input('Enter the units : ')
amt = 0;
if 1 <= units  <= 100:
    amt = units 
elif 1 <= units  <= 200:
    amt = units * 1.5
elif 1 <= units  <= 500:
    amt = (200 * 2) + (units - 200) * 3
elif units >  500:
    amt = (200 * 3) + (300 * 4) + (units - 500) * 5.75
else:
    print "%s : %s : invalid inputs" % (sys.argv[0], units)
    exit(1)
print "Billable : %.2f" % amt
 

