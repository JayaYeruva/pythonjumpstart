__author__ = 'ravi'

host = 'ws1.rootcap.in'
ip_addr = '192.11.1.1'
domain = 'rootcap.in'
"""
print "|{}|{}|{}|".format(host, ip_addr, domain)
print "|{:>22}|{:>16}|{:>16}|".format(host, ip_addr, domain)
print "|{:<22}|{:<16}|{:<16}|".format(host, ip_addr, domain)
print "|{:^22}|{:^16}|{:^16}|".format(host, ip_addr, domain)
"""

print "{:>6}  {}".format(1, host)
print "{:>6}  {}".format(2, ip_addr)
print "{:>6}  {}".format(3, domain)
