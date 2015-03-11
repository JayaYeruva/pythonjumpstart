__author__ = 'ravi'

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print mat[1]
#print mat[2]

mat[1][1] = 'x'
mat[2].append(10)

for row in mat:
    for col in row:
        print "{}\t".format(col),
    print