__author__ = 'ravi'

user_list = []

with open('/etc/passwd') as fp:
    for line in fp:
        if line.startswith('#'):
            continue
        user_list.append(line.split(':')[0].title())

content = ""
for index, login in enumerate(sorted(user_list), 1):
    content += "{:>6}  {}\n".format(index, login)

with open('userlist.dat', 'w') as fw:
    fw.write(content)
    print content.rstrip("\n")


