__author__ = 'ravi'
from pprint import  pprint

passwd = set(["root", 'bin', 'adm', 'nobody', 'apache', 'mysql'])
group = {"root", 'adm', 'mysql', 'pulse', 'admins', 'postgres'}


pprint(group | passwd)

"""
print passwd.difference(group)
pprint(passwd.union(group))
pprint(passwd.intersection(group))
"""


