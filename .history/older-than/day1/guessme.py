#!/usr/bin/env python
import random
rand = random.randint(1, 1000)

chance = 10
while chance >= 1:
    value = input('chance : %d\nEnter the number : ' % chance)

    if value == rand:
	print "You won :) !!!!!!!"
        exit(0)
    elif value < rand:
	print "%s : value is lesser" % value
    elif value > rand:
	print "%s : value is greater" % value
    chance -= 1

print "You lost, looser.... :(......."


