# brute force code, no from collections import Counter

num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_cust = int(input())
total = 0

for i in range(num_cust):
    order = list(map(int, input().split()))
    if order[0] in shoe_sizes:
        total += order[1]
        shoe_sizes.remove(order[0])

print(total)
