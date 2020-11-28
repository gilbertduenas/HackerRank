# https://www.hackerrank.com/challenges/utopian-tree/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    c = 1
    
    for i in range(n):
        if i % 2==0:
            c *= 2
        else:
            c += 1
            
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
