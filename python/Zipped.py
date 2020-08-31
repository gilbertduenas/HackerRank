# https://www.hackerrank.com/challenges/zipped/problem

n, x = map(int, input().split())

zipit = []

for i in range(x):
    zipit += [list(map(float, input().split()))]

for j in zip(*zipit):
    print(sum(j)/x)
