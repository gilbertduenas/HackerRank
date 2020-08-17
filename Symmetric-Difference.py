# Working with sets

index1 = input()
set1 = set(map(int, input().split()))
index2 = input()
set2 = set(map(int, input().split()))

final_set = set1.union(set2).difference(set1.intersection(set2))

for i in sorted(list(final_set)):
    print(i)
