# https://www.hackerrank.com/challenges/most-commons/problem

import math
import os
import random
import re
import sys

from collections import Counter, OrderedDict

class OrderedCounter(Counter):
    pass

if __name__ == '__main__':
    s = sorted(input())

    for c in OrderedCounter(s).most_common(3):
        print(f'{c[0]} {c[1]}')
        