__author__ = 'ravi'
from ops import get_size
from json import loads

result = loads(get_size())

print "{:>22} : {}".format("total", result.pop('total'))

for item in sorted(result):
    print "{:>22} : {}".format(item, result[item])

