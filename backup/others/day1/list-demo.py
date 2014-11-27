#!/usr/bin/env python

items = ['abab', 'alphine', 'abe',  'e', 'i', 'o', 'u', 1, 3 ,5 ,7];
print items[::2]
print items[1::2]

from random import shuffle
shuffle(items)

items.sort()
print items
