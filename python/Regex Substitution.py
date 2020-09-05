# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

n = int(input())

for i in range(n):
    l = input()
    
    while ' && ' in l or ' || ' in l:
        l = l.replace(' && ', ' and ').replace(' || ', ' or ')
    
    print(l)
