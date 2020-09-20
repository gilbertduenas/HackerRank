# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy

n = int(input())
j = []
k = []

for i in range(n):
    temp = list(map(int, input().split()))
    j.append(temp)

for i in range(n):
    temp = list(map(int, input().split()))
    k.append(temp)

print(numpy.dot(j, k))
