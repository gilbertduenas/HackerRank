# https://www.hackerrank.com/challenges/py-collections-deque/problem
# append, pop, popleft and appendleft

from collections import deque

n = int(input())
d = deque()

for i in range(n):
    command = list(input().split())

    if command[0] == 'append':
        d.append(command[1])
    elif command[0] == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()
    elif command[0] == 'appendleft':
        d.appendleft(command[1])

print(' '.join(d))
