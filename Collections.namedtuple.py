from collections import namedtuple

n = int(input())
student = namedtuple('student', input())
total = 0

for i in range(n):
    current = student(*input().split())
    total += int(current.MARKS)

print(total/n)
