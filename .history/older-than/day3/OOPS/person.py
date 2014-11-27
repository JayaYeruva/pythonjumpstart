#!/usr/bin/env python

class Person(object):
  def __init__(self, name, age, gender ):
    self.name = name
    self.age = age
    self.gender = gender

  def getInfo(self):
    print "Name   : %s " % self.name
    print "Age    : %s " % self.age
    print "Gender : %s " % self.gender


if __name__ == '__main__':
  p = Person('larry wall', '71', 'male')
  p.getInfo()
  print p.name
  print p.age
  print p.gender
  p.addr = '49, mg road, bangalore'
  print p.addr
