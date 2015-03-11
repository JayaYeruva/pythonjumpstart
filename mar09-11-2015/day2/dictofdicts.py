__author__ = 'ravi'
from pprint import pprint

info = dict()

with open('passwd') as fp:
    header = fp.readline().rstrip().split(',')[1:]
    #print header

    for line in fp:
        temp = line.rstrip().split(':')
        info[temp[0]] = dict(zip(header, temp[1:]))

pprint(info)

