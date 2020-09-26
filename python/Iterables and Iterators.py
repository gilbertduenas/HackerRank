# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

n = input()
N = input().split()
K = int(input())

c = list(combinations(N, K))
f = filter(lambda i: 'a' in i, c)

print(len(list(f))/len(c))
 
 