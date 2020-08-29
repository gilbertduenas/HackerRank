# https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy

input_list = list(map(int, input().split()))
an_array = numpy.array(input_list)

print(numpy.reshape(an_array, (3, 3)))
