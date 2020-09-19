# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy

n, m = map(int, input().split())
l = []

for i in range(n):
    temp = list(map(int, input().split()))
    l.append(temp)

sum_result = numpy.sum(l, axis=0)

print(numpy.prod(sum_result))
