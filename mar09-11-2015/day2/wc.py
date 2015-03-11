__author__ = 'ravi'
from os.path import isfile

file_name = 'message.txt'
wc = dict()

if isfile(file_name):
   for line in open(file_name):
       for word in line.rstrip().split(' '):
           if word in wc:
               wc[word] += 1
           else:
               wc[word] = 1


for word in wc:
    print "{:>6} : {}".format(wc[word], word)