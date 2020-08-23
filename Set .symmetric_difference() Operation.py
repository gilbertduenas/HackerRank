# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

i1 = input()
set1 = set(map(int, input().split()))
i2 = input()
set2 = set1.symmetric_difference(map(int, input().split()))

print(len(set2))
