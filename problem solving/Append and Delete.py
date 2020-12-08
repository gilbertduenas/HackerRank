# https://www.hackerrank.com/challenges/append-and-delete/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    i = 0
    
    while i<len(s) and i<len(t) and s[i]==t[i]:
        i+=1
        
    if (len(s)+len(t)-2*i)>k:
        return 'No'
    elif (len(s)+len(t)-k)<0 or (len(s)+len(t)-2*i)%2 == k%2:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
