# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re

n = int(input())
check = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
    
for i in range(n):
    if check.search(input().strip()):
        print('Valid')
        
    else: 
        print('Invalid')
