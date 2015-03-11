__author__ = 'ravi'
from pprint import pprint



with open('passwd') as fp:
    header = fp.readline().rstrip().split(',')[1:]

    info = {l.split(':')[0]: dict(zip(header, l.rstrip().split(':')[1:]))
                    for l in fp}


pprint(info)

