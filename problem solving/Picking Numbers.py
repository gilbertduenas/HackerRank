# https://www.hackerrank.com/challenges/picking-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
