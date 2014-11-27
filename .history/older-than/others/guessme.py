#!/usr/bin/python
import random
chance = 1
rand = random.randint(1, 1000)
while chance <= 10:
    value = input('chance : %s\nEnter the value :' % chance )
    if value == rand:
        print "You won :)...."
        exit(0)
    elif value < rand:
        print "%s: entered value was lesser" % value
    elif value > rand:
        print "%s: entered value was greater" % value
    chance += 1

print "You lost, looser :(......"
