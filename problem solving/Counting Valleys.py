# https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    level = 0
    valley = 0

    for i in path:
        if i == 'U':
            level += 1
        elif i == 'D':
            level -= 1

        if level == 0 and i == 'U':
            valley += 1

    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
