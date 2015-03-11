__author__ = 'ravi'
from fileinput import input
import re


def correct_it():
    regex = r"([a-z]{3})\ \ (\d\d?)\ (\d{2}:\d{2}:\d{2})"
    cmp = re.compile(regex, re.I)

    for l in input(inplace=True, backup='.bak'):
        print cmp.sub(r"[\3] \2 \1", l).rstrip()

correct_it()