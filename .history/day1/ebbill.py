#!/usr/bin/env python

def validate():
    print "invlid usage, try again"
    exit(1)
try:
    usage = input('Enter the usage :')
    if usage < 0:
        validate()
except:
    validate()

amt = 0

if usage <= 100:
    amt = usage
elif usage <= 200:
    amt = usage * 1.5
elif usage <= 500:
    amt = (200 * 2) + (usage - 200) * 3
elif usage > 500:
    amt = (200 * 3) + (300 * 4) + (usage - 500) * 5.75

print "billable : %.2f" % amt

