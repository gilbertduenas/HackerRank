# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

n = int(input())
items = OrderedDict()

for i in range(n):
  temp = input().split()
  alpha = [j for j in temp if j.isalpha()]
  key = ' '.join(alpha)
  value = temp[-1]

  # learn to rpartition and remove lines 7-10!
  # key, _, value = input().rpartition(' ')

  items[key] = items.get(key, 0) + int(value)

for key, value in items.items():
  print(key, value)
