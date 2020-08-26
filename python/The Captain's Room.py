# https://www.hackerrank.com/challenges/py-the-captains-room/problem

from collections import Counter

n = input()
d = list(map(str, input().split()))
ship = Counter(d)

for k,v in ship.items():
    if v == 1:
        print(k)
        break
