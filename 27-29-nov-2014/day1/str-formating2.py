#!/usr/bin/env python

name = 'henry'
age = 4
gender = 'male'

print "|{}|{}|{}|".format(name, age, gender)
print "|{:>22}|{:>5}|{:>10}|".format(name, age, gender)
print "|{:>22}|{:>5}|{:>10}|".format(name, age, gender)
print "|{:<22}|{:<5}|{:<10}|".format(name, age, gender)
print "|{:<22}|{:<5}|{:<10}|".format(name, age, gender)
print "|{0:^22}|{1:^5}|{2:^10}|".format(name, age, gender)
print "|{:^22}|{:^5}|{:^10}|".format(name, age, gender)
