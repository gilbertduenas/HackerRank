# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy

n = list(map(int, input().split()))
m = list(map(int, input().split()))

print(numpy.inner(n, m))
print(numpy.outer(n, m))
