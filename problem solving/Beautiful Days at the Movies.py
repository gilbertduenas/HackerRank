# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    d = int(0)
    
    for x in range(i, j+1):
        if (x - int(str(x)[::-1])) % k == 0:
            d += 1
            
    return d

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
