__author__ = 'ravi'
i = 1
while i <= 5:
    if i == 4:
        break
    elif i == 3:
        i += 1
        continue
    elif i == 1:
        print 'one'
    elif i == 2:
        print 'ii'
    else:
        print i
    i += 1
else:
    print "else block of the while loop"