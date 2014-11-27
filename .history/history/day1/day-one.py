# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# enumerate

# <codecell>

l = ['a', 'b', 'z']
for index, value in enumerate(l, 1):
    print index, value
    

# <codecell>

>>> mat = [[1,2,3], [4,5,6], [7,8,9]]
>>> 
>>> [row for row in mat]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> 
>>> 
>>> [row[1] for row in mat]
[2, 5, 8]
>>> 
>>> [col for row in mat for col in row ]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> [col for row in mat for col in row  if col % 2]
[1, 3, 5, 7, 9]
>>> 
>>> [col for row in mat if len(row) == 3 for col in row  if col % 2]

# <codecell>


