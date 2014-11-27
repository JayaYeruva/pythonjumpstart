#!/usr/bin/env python
import random
g_val = random.randint(1, 1000)
chance = 1
w_flag = 0
while chance <= 10:
    val = input("Chance : %d\nEnter the your prediction:" % chance)
    if g_val == val:
        print "You won :) !!!!"
        w_flag = 1
        break
    elif val > g_val:
	print "your value was greater"
    elif val < g_val:
	print "you value was lesser" 
    chance += 1

if w_flag == 0:
   print "You lost, looser :( ....."  
