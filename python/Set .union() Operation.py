# https://www.hackerrank.com/challenges/py-set-union/problem

i1 = input()
set1 = set(map(int, input().split()))
i2 = input()
set2 = set1.union(map(int, input().split()))

print(len(set2))
