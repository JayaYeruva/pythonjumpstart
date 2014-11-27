#!/usr/bin/env python
from random import randint

rand_value = randint(1, 1000)

i = 1
w_flag = 0
while i <= 10:
    value = input("Chance : %d\nEnter the value :" % i)
    if value == rand_value:
	print "You won :) !!!!!!!!! "
        w_flag = 1
        break
    elif value < rand_value:
	print "%d : entered value was lesser" % value
    elif value > rand_value:
	print "%d : entered value was greater" % value
    i += 1

if w_flag == 0:
    print "you lost, looser :(..............";
   
