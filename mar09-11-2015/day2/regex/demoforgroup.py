import re
import fileinput

pattern = re.compile('(\d{2})-(\d{2})-(\d{4})\ (\d{2}:\d{2}:\d{2})', re.I
)
for line in fileinput.input():
    m = pattern.search(line)
    if m:
        print m.group()
        print m.groups()
        exit(1)
