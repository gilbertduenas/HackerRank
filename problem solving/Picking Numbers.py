# https://www.hackerrank.com/challenges/picking-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    max = 0
    
    for i in l:
        c = l.count(i)
        d = l.count(i-1)
        c = c + d
        
        if c > max:
            max = c
    
    return max
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
