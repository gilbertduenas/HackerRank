# https://www.hackerrank.com/challenges/python-time-delta/problem

#!/bin/python3

from datetime import datetime as dt

import math
import os
import random
import re
import sys

def time_delta(t1, t2):
    f = '%a %d %b %Y %H:%M:%S %z'

    return str(int(abs((dt.strptime(t1, f) - dt.strptime(t2, f)).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()