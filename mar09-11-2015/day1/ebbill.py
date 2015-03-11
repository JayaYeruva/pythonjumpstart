__author__ = 'ravi'

amt = 0
units = input('Enter the units :')

if units <= 100:
    amt = units
elif units <= 200:
    amt = units * 1.5
elif units <= 500:
    amt = (200 * 2) + (units-200) * 3
elif units > 500:
    amt = (200 * 3) + (300 * 4) + (units-500) * 5.75

print "billable : {:.2f}".format(amt)

