# https://www.hackerrank.com/challenges/np-linear-algebra/problem

# Needed to peek at the discussion and added round().

import numpy

n = int(input())
det_list = []

for i in range(n):
    input_list = list(map(float, input().split()))
    det_list.append(input_list)

print(round(numpy.linalg.det(det_list), 2))
