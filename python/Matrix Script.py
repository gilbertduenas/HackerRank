# https://www.hackerrank.com/challenges/matrix-script/problem

#!/bin/python3

import math
import os
import random
import re
import sys

n = int((input().split())[0])
m = []
matrix = ''

for i in range(n):
    temp = input()
    m.append(temp)

for j in zip(*m):
    matrix += ''.join(j)

print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', matrix))
