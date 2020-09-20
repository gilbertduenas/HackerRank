# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy

numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
l = []

for i in range(n):
    temp = list(map(float, input().split()))
    l.append(temp)

print(numpy.mean(l, axis=1))
print(numpy.var(l, axis=0))
print(numpy.std(l))
