# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i

from collections import defaultdict

n, m = map(int, input().split())

a = defaultdict(list)
b = []

for i in range(n):
    a[input()].append(i+1)

for i in range(m):
    b.append(input())

for i in b: 
    if i in a:
        print(' '.join(map(str, a[i])))
    else:
        print(-1)


# i'm no genius, but i can understand when one speaks.
#from collections import defaultdict

#a = defaultdict(list)
#n, m = map(int, input().split())

#for i in range(n):
#    a[input()].append(str(i+1))

#for i in range(m):
#    print(' '.join(a[input()]) or -1)
