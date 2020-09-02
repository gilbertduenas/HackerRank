# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

n = int(input())

for i in  range(n):
    check = input()
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', check)))
