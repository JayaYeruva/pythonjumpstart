"""
a sample python module
"""
import os
import time


name = "intuit"
city = "bangalore"
version = "0.0.1 beta"

def ls(path="."):
    """
    list the content of the directory
    :param path: directory path
    :return: None
    """
    for name in os.listdir(path):
        print name,
    print


def get_file_times(filename):
    """
    get access, modified and change time of a file
    :param filename:
    :return:
    """
    stat = os.stat(filename)
    print "access time : {}".format(time.ctime(stat.st_atime))
    print "modify time : {}".format(time.ctime(stat.st_mtime))
    print "change time : {}".format(time.ctime(stat.st_ctime))


def power(x, n):
    """
    rasies x to the power of n
    :param x: int
    :param n: int
    :return: int
    """
    return x ** n

def main():
    print __name__  #refers the current namespace
    print power(5, 3)
    ls('.')
    get_file_times('/etc/passwd')

if __name__ == '__main__':
    main()
