#!/usr/bin/env python
target = 'testit.dat'
fn = raw_input('Enter the filename :')
i = 1

with open(target, 'w') as fw:
    with open(fn) as fp:
        for line in fp:
            content =  "{:>6}  {}".format(i, line.rstrip('\n'))
            print content
            fw.write(content+'\n')
            i += 1

