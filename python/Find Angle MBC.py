# https://www.hackerrank.com/challenges/find-angle/problem

# I don't know math functions

from math import *

a = float(input())
b = float(input())

print(str(int(round(degrees(atan(a/b)),0)))+'°')
