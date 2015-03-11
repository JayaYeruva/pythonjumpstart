__author__ = 'ravi'


s = "root:x:0:0:root:/root:/bin/bash"

passwd = s.split(":")[1:-1]

for item in passwd:
    print item

print "|".join(passwd)