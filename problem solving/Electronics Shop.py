# https://www.hackerrank.com/challenges/electronics-shop/problem

#!/bin/python3

import os
import sys
import itertools

def getMoneySpent(k, d, b):
    x = sorted([sum(i) for i in (itertools.product(k, d))], reverse=True)
    for i in x:
        if i <= b:
            return i
    
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    k = list(map(int, input().rstrip().split()))

    d = list(map(int, input().rstrip().split()))

    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    moneySpent = getMoneySpent(k, d, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
