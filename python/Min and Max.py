# https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy

n, m = map(int, input().split())
l = []

for i in range(n):
    temp = list(map(int, input().split()))
    l.append(temp)

min_result = numpy.min(l, axis=1)

print(numpy.max(min_result))
