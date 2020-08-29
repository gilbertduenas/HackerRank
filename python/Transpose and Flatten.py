# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy

n, m = map(int, input().split())
input_list =[]

for i in range(n):
    a = list(map(int, input().split()))
    input_list.append(a)

an_array = numpy.array(input_list)

print(numpy.transpose(an_array))
print(an_array.flatten())
