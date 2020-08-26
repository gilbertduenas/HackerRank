# https://www.hackerrank.com/challenges/py-check-subset/problem

n = int(input())

for i in range(n):
    a = input()
    a_set = set(map(int, input().split()))
    b = input()
    b_set = set(map(int, input().split()))

    print(a_set.issubset(b_set))
    
