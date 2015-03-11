__author__ = 'ravi'
import re

counter = 0


def fixit(m):
    global counter
    counter += 1
    return '*' if counter == 1 else m.groups()[0]


def replace(regex, replace_string, string):
    return re.sub(regex,  replace_string, string, flags=re.I)

content = replace("([AEIOU])", fixit,  "this is a sale string")
print content
