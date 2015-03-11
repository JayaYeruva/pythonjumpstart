__author__ = 'ravi'
from os.path import isfile

file_name = 'message.txt'
wc = dict()

if isfile(file_name):
   for line in open(file_name):
       for word in line.rstrip().split(' '):
           wc[word] = wc.get(word, 0) + 1


for word in wc:
    print "{:>6} : {}".format(wc[word], word)