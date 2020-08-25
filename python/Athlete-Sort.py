# https://www.hackerrank.com/challenges/python-sort-sort/problem
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

# My code
    arr.sort(key = lambda x: x[k]) 
    for i in arr:
        print(' '.join(str(x) for x in i))

# if i were smarter....
# N, M = map(int, input().split())
# rows = [input() for _ in range(N)]
# K = int(input())

# for row in sorted(rows, key=lambda row: int(row.split()[K])):
#     print(row)
