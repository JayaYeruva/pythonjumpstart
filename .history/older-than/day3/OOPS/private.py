#!/usr/bin/env python

class Person(object):
  def __init__(self, name, age, gender ):
    self.__name = name   #private attrib
    self.__age = age
    self.__gender = gender

  def __getInfo(self):  #private method
    print "Name   : %s " % self.__name
    print "Age    : %s " % self.__age
    print "Gender : %s " % self.__gender

  def getData(self):
    self.__getInfo()

  def __del__(self):
    print "%s destroying.........." % self

if __name__ == '__main__':
  p = Person('larry wall', '71', 'male')
  p.getData()
