__author__ = 'ravi'
from sys import path

path.insert(0, "/home/ravi/Training/Python-jumpstart/mar09-11-2015/lib")

from intutit import get_file_times, ls

ls('.')

get_file_times('testmod.py')
