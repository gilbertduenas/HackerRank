# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy

n = list(map(int, input().split()))

print(numpy.zeros(n, dtype = numpy.int))
print(numpy.ones(n, dtype = numpy.int))
