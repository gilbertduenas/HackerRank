# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

l =[]

for k, c in groupby(input()):
    l.append((len(list(c)), int(k)))

print(' '.join(map(str, l)))

