# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

s, n = map(str, input().split())

for i in combinations_with_replacement(sorted(s), int(n)):
    print(''.join(i))
