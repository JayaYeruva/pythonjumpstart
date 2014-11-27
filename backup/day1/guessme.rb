#!/usr/bin/env python

from random import randint,seed

seed()
wflag = 0
predict = randint(1,1000)
chance = 1
MAX = 10

while chance <= MAX:
    value = input('Chance: %s\nEnter the value : '% chance)
    if value == predict:
	print "You won :) !!!!!!!!!!!"
	wflag = 1
        break
    elif value < predict:
	print "%s is lesser" % value
    elif value > predict:
	print "%s is greater" % value
    chance += 1

if wflag == 0:
    print "You lost, looser :(........."
    exit(1)
