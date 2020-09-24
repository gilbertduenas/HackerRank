# https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

n = int(input())
d = OrderedDict()

for i in range(n):
    k = input()

    if not k in d.keys():
        d.update({k:1})
        continue
    
    d[k] += 1

print(len(d.keys()))
print(*d.values())
