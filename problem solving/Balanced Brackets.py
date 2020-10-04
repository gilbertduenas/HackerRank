# https://www.hackerrank.com/challenges/balanced-brackets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    start = ['[', '{', '(']
    close = [']', '}', ')']
    valid = []
    
    for i in s:
        if i in start:
            valid.append(i)
        elif i in close:
            index = close.index(i)
            if ((len(valid) > 0) and (start[index] == valid[len(valid)-1])):
                valid.pop()
            else:
                return 'NO'
                
    if len(valid) == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
