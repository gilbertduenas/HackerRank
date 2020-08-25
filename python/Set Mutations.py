# https://www.hackerrank.com/challenges/py-set-mutations

n = input()
s = set(map(int, input().split()))
t = int(input())

for i in range(t):
    command = list(input().split())
    s2 = set(map(int, input().split()))
    
    if command[0] == 'update':
        s.update(s2)
    elif command[0] == 'intersection_update':
        s.intersection_update(s2)
    elif command[0] == 'difference_update':
        s.difference_update(s2)
    elif command[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(s2)

print(sum(s))
