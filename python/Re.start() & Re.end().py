# https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

S = input()
k = input()

pattern = re.compile(k)
r = pattern.search(S)

if !r: 
    print('(-1, -1)')

while r:
    a = r.start()
    b = r.end() - 1
    print(f'({a}, {b})')
    
    r = pattern.search(S, a + 1)
