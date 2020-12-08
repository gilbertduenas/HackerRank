# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    l = math.sqrt(a)
    m = math.sqrt(b)
    x = int(m)-int(l)
    
    if float(l) - int(l) == 0:
        x += 1
        
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
