from itertools import permutations

input_list = list(map(str, input().split()))

for i in sorted(list(permutations(input_list[0], int(input_list[1])))):
    print(''.join(i))
