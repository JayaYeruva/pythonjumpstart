#!/usr/bin/python

def kwargs(**args):
    print args

passwd = {'uid':0, 'dir':'/root', 'shell':'/bin/bash'}
kwargs()
kwargs(name='python', version='2.7.8', arch='x86_64')
kwargs(id=1001, fname='neil', lname='jcakson', gender='male') 
kwargs(**passwd)
