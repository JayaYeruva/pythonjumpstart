__author__ = 'ravi'


def center(str_content, width, fill=" "):
    n = (width - len(str_content)) / 2
    return "{}{}{}".format(fill * n, str_content, fill * n)


print center('perl', 10, '-')
print center('perl', 10)
print "perl".center(10)
