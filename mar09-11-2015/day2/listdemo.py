__author__ = 'ravi'

l = [3, 4, 2, 6]

temp = []  #1. empty list

for item in l:   #2. iter
    temp.append(item ** item)   #computed & append to empty list

print temp

op = [i**i for i in l]   #list comp
print op