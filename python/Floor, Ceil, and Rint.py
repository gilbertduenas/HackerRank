# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy

numpy.set_printoptions(sign=' ')
n = list(map(float, input().split()))

print(numpy.floor(n))
print(numpy.ceil(n))
print(numpy.rint(n))
