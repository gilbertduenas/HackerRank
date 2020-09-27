# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

n = int(input())

for i in range(n):
    m = input()
    l = deque(map(int, input().split()))

    for c in reversed(sorted(l)):
        if l[-1] == c: 
            l.pop()
        elif l[0] == c: 
            l.popleft()
        else:
            print('No')
            break
    else: print('Yes')

