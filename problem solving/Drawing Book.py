# https://www.hackerrank.com/challenges/drawing-book/problem

#!/bin/python3

import os
import sys

def pageCount(n, p):

    try :
        return min(p//2, n//2 - p//2)

    except (RuntimeError, ValueError):                         
        print(1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
