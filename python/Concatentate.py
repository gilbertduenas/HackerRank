# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy

n, m, p = map(int, input().split())

array1 = [list(map(int, input().split())) for i in range(n)]
array2 = [list(map(int, input().split())) for i in range(m)]

print(numpy.concatenate((array1, array2), axis=0))